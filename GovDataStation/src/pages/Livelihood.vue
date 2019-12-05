<template>
  <div class="content">
    <div class="container-fluid">
      <div class="main_page">
        <div class="login" v-if="!loginStatus">
          <iframe
            id="myframe"
            name="myframe"
            :src="src"
            ref="iframe"
            scrolling="no"
            width="350px"
            height="350px"
            frameborder="0"
          ></iframe>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  mounted() {
  
    window.addEventListener('message', this.handleMessage);
    this.iframeWin = this.$refs.iframe.contentWindow;
    
  },
   methods: {
     handleMessage (event) {
       const data = event.data.data
        if(data.code === "success"){
            alert(data.test)
        }
     }
}
};
</script>
