# PyfUS (v0.1)

The Python functional ultrasound brain imaging analysis package. This package is currently under development.

## **Installation**

Before you start the installation, ensure that you have Python installed on your system. This package requires Python version 3.6 or above.

Follow the steps below to install the package:

1. Clone the repository:

> `git clone https://github.com/Senzt/PyfUS.git`

2. Navigate to the cloned directory

> `cd PyfUS`

3. Install the package: you can install the package using pip. If the package includes a setup.py file, use the following command:

> `pip install .`

In Colab:

> `!pip install git+https://github.com/Senzt/PyfUS.git`

## **Exploring the Functions and Capabilities of the Package**

1.  **Data loading** (50% done): The package can handle fUS data in .mat files only. It allows users to access, read, and store all .mat files located within subfolders of a directory, *ensuring a smooth and efficient data ingestion process.*
> **Challenge:** The absence of a standardized fUS storage format hinders generic data import. Without a consistent method for importing fUS data, its accessibility and usability are limited. A future BIDS extension tailored for fUS could simplify data import and enhance its utility across various sources. Researchers would benefit from easier loading and analysis of fUS data from diverse studies and institutions.

2.  **Flexible data handling:** (?% done) The package is designed to work with dictionaries containing lists of fUS data, allowing users to handle multiple data sets simultaneously.
> **Challenge:** Given my limited experience in deep analysis of this specific data type, I am uncertain about the usefulness of storing it in the current format.

3.  **Data visualization (90%? done based on the plan):** Users can plot CBV% over time and generate fUS images with energy level representations.
> **Challenge:** At this stage, I am unsure about the specific information that needs to be presented and how to appropriately normalize the data.

4.  **Interactivity:** The package includes functions that incorporate interactivity, such as browsing through fUS images one at a time using the interact function. This enables users to view fUS images at different time points interactively.
> **Future Improvement:** Zoom in on specific areas of interest.

5.  **Cerebral Blood Volume (CBV) conversion:** The package can convert fUS image data, which are typically represented as a 4-dimensional array (x, y, z, time), into CBV%. It achieves this by averaging over the first few frames to create a baseline, and then computes the CBV% using the provided formula.
> **Challenge:** I am unsure if my current CBV% calculation is correct. Further studies are required.

6.  **Epoching:** The package provides the functionality to slice the time dimension of the data into epochs based on given start and stop time points, and can calculate the mean, min, and max CBV% over time for each epoch. Users can visualize these epochs with highlighting of the selected time span and vertical lines indicating start and stop points.

## **Summary**

**Main Challenge:**

> I currently have limited understanding of how to handle the data effectively, but as I continue to learn and gain more knowledge, I believe it will greatly enhance the capabilities of this package.

**Future Improvements:**

1.  **Masking system:** We need to select a region of interest (ROI) to proceed with further preprocessing. Masking processing is necessary.
2.  **Pre-processing (denoising) pipeline:** There are additional crucial steps to preprocess the data, such as denoising. However, a deeper understanding of the data itself and the extraction components is required to implement them effectively.
3.  **Improved visualization:** Currently, the visualization is limited to plt.plot! It would be beneficial to enhance the visualization capabilities.
4.  **Memory optimization:** The current version may encounter out-of-memory issues when dealing with larger data. A well-planned architecture is needed to address this.
5.  **Computation optimization:** The processing speed has not been considered yet. A good package should have proper optimization techniques in place.
