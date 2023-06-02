import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
from ipywidgets import interact, widgets
import glob
import os

class io:    
 
    def read_doppler(self, directory_patch, probe_type):
        
        PD_image_folder = glob.glob(directory_patch + '/FilteredData/*')
        #print(PD_image_folder)
        Mask_folder = glob.glob(directory_patch + '/MaskData/*')
        #print(Mask_folder)
        Info_folder = glob.glob(directory_patch + '/InfoData/*')
        #print(Info_folder)
        
        PD_dict = {}
        Mask_list = []
        Info_list = []
     
        FolderNum = 1
        
        for PD_filename in PD_image_folder:            
            
            PD_sub_folder = glob.glob(PD_filename +'/*')
            
            PD_sub_list = []
            
            for PD_sub_filename in PD_sub_folder:                            
                
                MatRead = sio.loadmat(PD_sub_filename)
                #print(MatRead.keys())
                PD_sub_list.append(MatRead['b0'])
            # self.mask = np.array(Mask_list)
            PD_dict[FolderNum] = PD_sub_list
            FolderNum = FolderNum + 1
        
        self.PD_full = PD_dict
        
        raw_dict = self.calculate_mean_over_raw(PD_dict)
        self.raw_dict = raw_dict
        # return PD_dict
        
        for Mask_filename in Mask_folder:
            MatRead = sio.loadmat(Mask_filename)
            #print(MatRead.keys())
            Mask_list.append(MatRead['ACx'])
        self.mask = np.array(Mask_list)
        
        # # This is complicated structor
        # for Info_filename in Info_folder:
        #     MatRead = sio.loadmat(Info_filename)
        #     #print(MatRead.keys())            
        #     self.exptevents = MatRead['exptevents']
        #     self.exptparams = MatRead['exptparams'] 
        #     self.globalparams = MatRead['globalparams']
        
        cbv_dict = self.calculate_cbv_percent(PD_dict)
        mean_dict = self.calculate_mean_over_images(cbv_dict)
        #self.plot_cbv_percent(cbv_dict)
        
        self.cbv_dict = cbv_dict
        self.mean_dict = mean_dict
        
        
    def calculate_cbv_percent(self, images_dict):
        
        cbv_dict = {}
        for key, images in images_dict.items():
            images = np.array(images)  # Convert list to NumPy array
            baseline = np.mean(images[:, :, :8], axis=2)  # assuming first 10 frames as baseline
            cbv_dict[key] = ((images - baseline[:, :, None]) / baseline[:, :, None]) * 100
                 
        return cbv_dict
    
    def calculate_mean_over_images(self, data_dict):
        
        mean_dict = {}
        for key, data in data_dict.items():
            data = np.array(data)  # Ensure data is a numpy array for multidimensional indexing
            mean_data = np.mean(data, axis=(1, 2))  # Compute the mean over the second and third dimensions
            mean_dict[key] = mean_data
    
        return mean_dict


    def plot_cbv_percent(self):
        
        for key, data in self.mean_dict.items():
            
            for ss in range(0, len(data)):
                plt.plot(data[ss])
                
        plt.xlabel('Time point')
        plt.ylabel('CBV %')        
        plt.show()
        
        for key, data in self.mean_dict.items():
            
            mean_data = np.mean(data, axis=0)
            min_data = np.min(data, axis=0)
            max_data = np.max(data, axis=0)
            
            time_points = range(mean_data.shape[0])
            plt.plot(time_points, mean_data, label=key)
            plt.fill_between(time_points, min_data, max_data, alpha=0.1)
                
        plt.xlabel('Time point')
        plt.ylabel('CBV %')    
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  
        plt.show()  
        
    #################################################################
        
    def calculate_mean_over_raw(self, data_dict):
        
        mean_dict = {}
        for key, data_list in data_dict.items():
            # Convert the list of arrays into a 4D array
            data = np.stack(data_list, axis=0)  # The resulting shape is (240, 49, 128, 19)
            # Compute the mean over the second and third dimensions
            mean_data = np.mean(data, axis=(1, 2))  # The resulting shape is (240, 19)
            mean_dict[key] = mean_data
    
        return mean_dict
    
    def plot_raw_pd(self):
        
        for key, data in self.raw_dict.items():
            
            for ss in range(0, len(data)):
                plt.plot(data[ss])
                
        plt.xlabel('Time point')
        plt.ylabel('CBV %')        
        plt.show()
        
        for key, data in self.raw_dict.items():
            
            #print(data.shape)
            #plt.plot(np.mean(data,axis=0),label=key)
            
            mean_data = np.mean(data, axis=0)
            min_data = np.min(data, axis=0)
            max_data = np.max(data, axis=0)
            
            time_points = range(mean_data.shape[0])
            plt.plot(time_points, mean_data, label=key)
            plt.fill_between(time_points, min_data, max_data, alpha=0.1)
                
        plt.xlabel('Time point')
        plt.ylabel('CBV %')    
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')  
        plt.show()     

    #################################################################
    
    def plot_fUS_image(self, session, trial):
        fUS_selected = self.PD_full[session]
        fUS_selected = fUS_selected[trial]
        n = fUS_selected.shape[2]  # the number of subplots
    
        fig, axs = plt.subplots(nrows=n, ncols=1, figsize=(7,50))
    
        for i in range(n):
            energy = np.sum(fUS_selected[:,:,i]**2)  # Compute the energy of the image
            axs[i].imshow(fUS_selected[:,:,i], cmap='viridis')  # Add the 'viridis' colormap
            axs[i].set_title(f'fUS image at {i} seconds - Energy: {energy:.2f}')
    
        plt.xlabel('Pixel X')
        plt.ylabel('Pixel Y')
        plt.tight_layout()
        plt.show()
    
    #################################################################
        
    def plot_fUS_slide(self, session, trial):
        
        fUS_selected = self.PD_full[session]
        fUS_selected = fUS_selected[trial]
        n = fUS_selected.shape[2]  # the number of subplots
        
        def view_image(i):
            energy = np.sum(fUS_selected[:,:,i]**2)  # Compute the energy of the image
            plt.imshow(fUS_selected[:,:,i], cmap='viridis')  # Add the 'viridis' colormap
            plt.title(f'Time step: {i} - Energy: {energy:.2f}')
            plt.xlabel('Pixel X')
            plt.ylabel('Pixel Y')
            plt.show()
    
        interact(view_image, i=(0,n-1))
        
    #################################################################
    #################################################################
    #################################################################
    
    ####################### Single function #########################
    
    def read_doppler_single(self, file_patch):
        
        ####################################
        
        self.mat = sio.loadmat(file_patch)
        
        sorted(self.mat.keys()) 
        #print(self.mat.keys())
        # Fix this
        self.data = self.mat['b0']        
        
        ####################################
        
        self.bloodflow = []        
        calibration_factor = 0.01        
        
        for t in range(self.data.shape[2]):
        
            # Select the image at time t
            image_t = self.data[:, :, t]
        
            # Extract the ROI from the image
            #roi = image_t[roi_top:roi_bottom, roi_left:roi_right]
            roi = image_t
        
            # Compute the mean pixel intensity in the ROI
            mean_intensity = np.mean(roi)
        
            # Convert the mean pixel intensity to blood flow using the calibration factor
            flow = mean_intensity * calibration_factor
        
            # Append the calculated blood flow to the list
            self.bloodflow.append(flow)
            
        self.bloodflow = np.array(self.bloodflow)
        
        ##################################

        print("Loading successful.")
        
    def plot_CBV_single(self):
        # Plot the blood flow over time
        plt.plot(self.bloodflow)
        plt.xlabel('Time point')
        plt.ylabel('CBV %')
        plt.show()
        
        ##################################
        
    def plot_fUS_single(self):
        
        n = self.data.shape[2]  # the number of subplots

        fig, axs = plt.subplots(nrows=n, ncols=1, figsize=(15,100))
        
        for i in range(n):
            axs[i].imshow(self.data[:,:,i])
            axs[i].set_title('the blood flow')
        
        plt.show()
        
        
    def browse_images_single(self):
        n = self.data.shape[2]
        def view_image(i):
            plt.imshow(self.data[:,:,i], interpolation='nearest')
            plt.title(f'Time step: {i}')
            plt.show()
        interact(view_image, i=(0,n-1))
    