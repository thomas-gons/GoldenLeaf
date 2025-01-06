<template>
    <div class="gallery" v-if="images.length > 0">
      <div
        v-for="(image, index) in images"
        :key="index"
        class="image-container"
        @click="selectImage(image)"
      >
          <img :src="image" alt="Plant Image" />
      </div>
      <div class="selected-image" v-if="selectedImage">
        <div id="preview-container">
          <img :src="selectedImage" alt="Selected Image">
          <div id="close-preview" @click="close()">✕</div>
        </div>
      </div>
    </div>
  </template>


<script>
export default {
  props: {
    images: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      selectedImage: null // L'image actuellement sélectionnée
    };
  },
  methods: {
    selectImage(image) {
      this.selectedImage = image; // Met à jour l'image sélectionnée
    },

    close() {
      this.selectedImage = null;
    }
  }
};
</script>
  <style scoped>
.gallery {
  margin: 0 auto;
  width: 40%;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 1em;
  justify-content: center;
  background-color: #f4f4f4;
  border-radius: 8px;
}

.image-container {
  width: 150px;
  height: 150px;
  border: 1px solid #dde1e6;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
  cursor: pointer; /* Curseur de pointeur pour montrer que c'est cliquable */
}

.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.selected-image {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
}

.selected-image img {
  max-width: 100%;
  max-height: 100%;
  border: 1px solid #dde1e6;
  border-radius: 8px;
  box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.2);
}

#preview-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 85%;
  position: relative;
}

#close-preview {
  position: absolute;
  top: -10px;
  right: -10px;
  color: white;
  background-color: #ec4d4d;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 18px;
  font-weight: 700;
  border: none;
  cursor: pointer;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
  z-index: 20;
}

#close-thumbnail:hover {
  background-color: darkred;
}
</style>
