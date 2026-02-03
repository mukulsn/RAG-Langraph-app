"""
UI components for the Advanced RAG application
"""
import streamlit as st
from config import (
    PAGE_TITLE, PAGE_ICON, LAYOUT, SIDEBAR_STATE,
    FILE_CATEGORIES, UPLOAD_PLACEHOLDER_TITLE, UPLOAD_PLACEHOLDER_TEXT
)
from utils import formate_file_size

def render_file_analysis(file_info):
    """Shows file analysis metrics"""
    st.markdown("### File Analysis")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("** Filename**")
        st.write(file_info['filename'])

    with col2:
        st.markdown("** Size**")
        size_display = formate_file_size(file_info['size'])
        st.write(size_display)

    with col3:
        st.markdown("** Type**")
        st.write(f".{file_info['extension'].upper()}")

    with col4:
        st.markdown("** Status**")
        status_icon = "✅" if file_info['is_supported'] else "Unsupported"
        status_text = "Supported" if file_info['is_supported'] else "Unsupported"
        st.write(f"{status_icon} {status_text}")