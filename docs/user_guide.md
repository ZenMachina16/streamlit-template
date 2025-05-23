# User Guide

Welcome to the OpenMS Streamlit Web Application! This guide will help you understand how to use our tools effectively.

## Advantages of OpenMS Web Apps

OpenMS web applications provide a user-friendly interface for accessing the powerful features of OpenMS. Here are a few advantages:
- **Accessibility**: Access powerful OpenMS algorithms and TOPP tools from any device with a web browser.
- **Ease of Use**: Simplified user interface makes it easy for both beginners and experts to perform complex analyses.
- **No Installation Required**: Use the tools without the need to install OpenMS locally, saving time and system resources.

## Workspaces

In the OpenMS web application, workspaces are designed to keep your analysis organized:
- **Workspace Specific Parameters and Files**: Each workspace stores parameters and files (uploaded input files and results from workflows).
- **Persistence**: Your workspaces and parameters are saved, so you can return to your analysis anytime and pick up where you left off. Simply bookmark the page!


### File Uploads
- **Online Mode**: You can upload only one file at a time. This helps manage server load and optimizes performance.

- **Local Mode**: Multiple file uploads are supported, giving you flexibility when working with large datasets. Additionally, the file size upload limit can be adjusted in the following ways:
  1. **Using `.streamlit/config.toml`**:
     - You can modify the `.streamlit/config.toml` file and set the `maxUploadSize` parameter to your desired value. By default, this is set to 200MB.
     - Example:
       ```toml
       [server]
       maxUploadSize = 500  # Set the upload limit to 500MB
       ```
  2. **Using CLI Command**:
     - You can customize the file size upload limit directly when running the application using the `--server.maxUploadSize` argument.
     - Example:
       ```bash
       python run_app.py --server.maxUploadSize 500
       ```
     - This sets the upload limit to 500MB for the current session.
     
- **Workspace Access**:
  - In online mode, workspaces are stored temporarily and will be cleared after seven days of inactivity.
  - In local mode, workspaces are saved on your local machine, allowing for persistent storage. Workspace directory can be specified in the `settings.json`. Defaults to `..` (parent directory).

## Downloading Results

You can download the results of your analyses, including data, figures and tables, directly from the application:
- **Figures**: Click the camera icon button, appearing while hovering on the top right corner of the figure. Set the desired image format in the settings panel in the side bar.
- **Tables**: Use the download button to save tables in *csv* format, appearing while hovering on the top right corner of the table.
- **Data**: Use the download section in the sidebar to download the raw results of your analysis.

## Getting Started

To get started:
1. Select or create a new workspace.
2. Upload your data file.
3. Set the necessary parameters for your analysis.
4. Run the analysis.
5. View and download your results.

For more detailed information on each step, refer to the specific sections of this guide.