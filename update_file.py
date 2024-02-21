import streamlit as st
import os
import base64
import secrets


@st.cache_resource
def get_csrf_token():

    return base64.b64encode(secrets.token_bytes(32)).decode("utf-8")


def update_file_into_server(car_name, List_file, csrf_token):
    if csrf_token != get_csrf_token():
        st.error("Invalid CSRF token. This request is not allowed.")
        return
    if car_name!="" :
        car_name=str(car_name).upper()
        folder_save_file_upload = os.path.join('data', car_name)
        if not os.path.exists(folder_save_file_upload):
            os.makedirs(folder_save_file_upload)
        for file in List_file:
            file_path = os.path.join(folder_save_file_upload, file.name)
            with open(file_path, "wb") as f:
                f.write(file.getvalue())
        if len(List_file)!=0:
            st.write("Update File Completed!!!")
