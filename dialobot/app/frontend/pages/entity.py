import streamlit as st



def page():
    st.title('Entity Recognition')
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(
        "Entity recognition is a feature that extracts the entity in the user's utterance. "
        "Dialobot can predict the entity in the user's utterances with just a few examples without training. "
        "You can edit by clicking name of entity, "
        "and if you want to add a new entity, click the 'Add Entity' button."
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("***")

    col1, col2 = st.beta_columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center'>Entity Name</h4>",
                    unsafe_allow_html=True)
    with col2:
        st.markdown("<h4 style='text-align: center'>Registered Words</h4>",
                    unsafe_allow_html=True)

    st.markdown("***")

    col1, col2 = st.beta_columns(2)
    with col1:
        st.button("Pizza")
        st.button("Location")

    with col2:
        st.markdown("<p style='text-align: center; padding: 0.25rem 0.25rem;'> 25 </p>",
                    unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; padding: 0.25rem 0.25rem;'> 104 </p>",
                    unsafe_allow_html=True)

    st.markdown("***")
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("Add Entity")
    st.markdown("<br>", unsafe_allow_html=True)
