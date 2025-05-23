import streamlit as st
from pathlib import Path
import json
# For some reason the windows version only works if this is imported here
import pyopenms

if "settings" not in st.session_state:
        with open("settings.json", "r") as f:
            st.session_state.settings = json.load(f)

if __name__ == '__main__':
    pages = {
        str(st.session_state.settings["app-name"]) : [
            st.Page(Path("content", "quickstart.py"), title="Quickstart", icon="👋"),
            st.Page(Path("content", "documentation.py"), title="Documentation", icon="📖"),
        ],
        "TOPP Workflow Framework": [
            st.Page(Path("content", "topp_workflow_file_upload.py"), title="File Upload", icon="📁"),
            st.Page(Path("content", "topp_workflow_parameter.py"), title="Configure", icon="⚙️"),
            st.Page(Path("content", "topp_workflow_execution.py"), title="Run", icon="🚀"),
            st.Page(Path("content", "topp_workflow_results.py"), title="Results", icon="📊"),
        ],
        "pyOpenMS Workflow" : [
            st.Page(Path("content", "file_upload.py"), title="File Upload", icon="📂"),
            st.Page(Path("content", "raw_data_viewer.py"), title="View MS data", icon="👀"),
            st.Page(Path("content", "run_example_workflow.py"), title="Run Workflow", icon="⚙️"),
            st.Page(Path("content", "download_section.py"), title="Download Results", icon="⬇️"),
        ],
        "Others Topics": [
            st.Page(Path("content", "simple_workflow.py"), title="Simple Workflow", icon="⚙️"),
            st.Page(Path("content", "run_subprocess.py"), title="Run Subprocess", icon="🖥️"),
        ]
    }

    pg = st.navigation(pages)
    pg.run()