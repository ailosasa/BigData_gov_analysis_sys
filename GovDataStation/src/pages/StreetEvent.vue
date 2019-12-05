<template>
  <div class="content">
    <div class="container-fluid">
      <div class="main_page">
        <button v-on:click="load">load</button>
        <!-- <iframe id="bdpic" src="/hot_community.html" frameborder="0" width="100%" height="100%"></iframe> -->
        <iframe
          id="bdpic"
          src="http://127.0.0.1:53051/hot_community.html"
          frameborder="0"
          width="100%"
          height="100%"
        ></iframe>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data(){
    return{
     data :[
    {name:'汤坑社区', value:100},
    {name:'坪山社区', value:200},
    {name:'南布社区', value:300},
    {name:'和平社区', value:400},
    {name:'田心社区', value:500},
    {name:'金沙社区', value:600}
],
geoCoordMap :{
    '龙田社区':[114.372841,22.753346],
    '汤坑社区':[114.331079,22.678805],
    '坪山社区':[114.353907,22.69667],
    '南布社区':[114.375607,22.70534],
    '和平社区':[114.355104,22.697106],
    '金沙社区':[114.406008,22.75079],
    '田心社区':[114.421943,22.700351]

}
    }
  },
  methods:{
    load(){
      var message = {data:this.data,geoCoordMap:this.geoCoordMap}
      var myframe = document.getElementById('bdpic');//获取iframe
      var childDomain = "http://127.0.0.1:53051/hot_community.html"
      var b=myframe.contentWindow.postMessage({
        data: message},"*");
        debugger
    }
  }
}
</script>
