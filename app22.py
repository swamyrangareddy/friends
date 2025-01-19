import streamlit as st

# Set the page title
st.set_page_config(page_title="Photo Gallery App")

# Define the photos and titles
photo_data = {
    "Kobbari Bondam": [
        {"image": "img 1.jpg", "title": "Design 1"},
        {"image": "img 2.jpg", "title": "Design 2"},
        {"image": "img 3.jpg", "title": "Design 3"},
        {"image": "img 4.jpg", "title": "Design 4"},
        {"image": "img 5.jpg", "title": "Design 5"},
        {"image": "img 6.jpg", "title": "Design 6"},
        {"image": "img 7.jpg", "title": "Design 7"},
        {"image": "img 8.jpg", "title": "Design 8"},
        {"image": "img 9.jpg", "title": "Design 9"},
        {"image": "img 10.jpg", "title": "Design 10"},
        {"image": "img 11.jpg", "title": "Design 11"},
        {"image": "img12.jpg", "title": "Design 12"},
        {"image": "img 13.jpg", "title": "Design 13"},
        {"image": "img 14.jpg", "title": "Design 14"},
        {"image": "img 15.jpg", "title": "Design 15"},
        {"image": "img 16.jpg", "title": "Design 16"},
        {"image": "img 17.jpg", "title": "Design 17"},
        {"image": "img 18.jpg", "title": "Design 18"},
        {"image": "img 19.jpg", "title": "Design 19"},
        {"image": "img 20.jpg", "title": "Design 20"},
    ],
    "Adduthera": [
        {"image": "img 101.jpg", "title": "Design 1"},
        {"image": "img 102.jpg", "title": "Design 2"},
        {"image": "img 103.jpg", "title": "Design 3"},
        {"image": "img 104.jpg", "title": "Design 4"},
        {"image": "img 105.jpg", "title": "Design 5"},
    ]
}

# Create a sidebar for tabs
selected_tab = st.sidebar.selectbox(
    "Select a tab",
    ["Kobbari Bondam", "Adduthera"]
)

# Display the selected tab's photos
tabs = st.tabs(["Kobbari Bondam", "Adduthera"])

# Display photos for each tab
for tab_name, tab in zip(photo_data.keys(), tabs):
    with tab:
        st.title(tab_name)
        photos = photo_data[tab_name]
        cols = st.columns(2)
        for idx, photo in enumerate(photos):
            with cols[idx % 2]:
                st.image(photo["image"], width=300)
                st.write(photo["title"])
                st.markdown("---")

            st.markdown("---")
else:
    st.write("No photos available for this tab.")
