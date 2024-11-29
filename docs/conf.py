"""Configuration file for the Sphinx documentation builder."""

external_projects_local_file = "projects.yaml"
external_projects_remote_repository = ""
external_projects = ["amd-gpu-operator"]
external_projects_current_project = "amd-gpu-operator"

project = "AMD Instinct Hub"
version = "1.0.0"
release = version
html_title = f"AMD GPU Operator {version}"
author = "Advanced Micro Devices, Inc."
copyright = "Copyright (c) 2024 Advanced Micro Devices, Inc. All rights reserved."

# Required settings
html_theme = "rocm_docs_theme"
main_doc_link = {
    "Instinct&#8482 Hub": "https://dcgpu.docs.amd.com"
},
html_theme_options = {
    "flavor": "instinct"
    # Add any additional theme options here
}
extensions = ["rocm_docs"]

# Table of contents
external_toc_path = "./sphinx/_toc.yml"

exclude_patterns = ['.venv']
