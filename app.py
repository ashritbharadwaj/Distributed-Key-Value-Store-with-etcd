import streamlit as st
from etcd import *
import etcd3

# Initialize etcd client
etcd_client = etcd3.client(host='localhost', port=1111)

st.title('ETCD Operations')

# Menu for operations
operation = st.selectbox('Choose an operation', ['Get all keys', 'Get key value', 'Insert key-value', 'Delete key', 'Connect to etcd'])

if operation == 'Get all keys':
    keys = get_all_etcd_keys(etcd_client)
    st.write(keys)

elif operation == 'Get key value':
    key = st.text_input('Enter the key')
    if st.button('Get value'):
        value = get_etcd_key_value(etcd_client, key)
        st.write(f'Value for key "{key}": {value}')

elif operation == 'Insert key-value':
    key = st.text_input('Enter the key')
    value = st.text_input('Enter the value')
    if st.button('Insert key-value'):
        success = insert_etcd_key_value(etcd_client, key, value)
        st.write('Key-value inserted successfully' if success else 'Key-value insertion failed')

elif operation == 'Delete key':
    key = st.text_input('Enter the key')
    if st.button('Delete key'):
        success = delete_etcd_key(etcd_client, key)
        st.write('Key deleted successfully' if success else 'Key deletion failed')

elif operation == 'Connect to etcd':
    # host = st.text_input('Enter host', value='localhost')
    # port = st.number_input('Enter port', value=2379)
    if st.button('Connect'):

        success = connect_to_etcd(host='localhost', port=1111)
        st.write(f'Connected successfully' if success else 'Connection failed')