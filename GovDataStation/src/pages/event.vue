<template>
  <div class="vueBox">
    <div class="marquee1">
      <div class="marquee_title1">
        <span>异常事件报警</span>
      </div>
      <div class="marquee_box1">
        <ul class="marquee_list1" :class="{ marquee_top1: animate }">
          <li v-for="(item, index) in marqueeList" :key="index">
            <span>在</span>
            <span class="red"> {{ item.COMMUNITY_NAME }}</span>
            <span>发生</span>
            <span class="red"> {{ item.EVENT_TYPE_NAME }}</span>
            <span>事件投诉</span>
            <span class="red"> {{ item.num }}</span>
            <span>起，请尽快前往处理</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
import axios from "axios";
export default {
  data: function() {
    return {
      animate: false,
      marqueeList: [
        {
          CREATE_TIME: "2018-07-04 17:24:41",
          STREET_NAME: "龙田街道",
          COMMUNITY_NAME: "南布社区",
          EVENT_SRC_NAME: "12345",
          SUB_TYPE_NAME: "市容环卫",
          EVENT_PROPERTY_NAME: "投诉",
          DISPOSE_UNIT_NAME: "龙田街道综合执法队"
        },
        {
          CREATE_TIME: "2018-07-07 17:24:41",
          STREET_NAME: "坪山街道",
          COMMUNITY_NAME: "和平社区",
          EVENT_SRC_NAME: "12345",
          SUB_TYPE_NAME: "工业废气",
          EVENT_PROPERTY_NAME: "投诉",
          DISPOSE_UNIT_NAME: "环境保护和水务局"
        },
        {
          CREATE_TIME: "2018-07-08 17:24:41",
          STREET_NAME: "失败街道",
          COMMUNITY_NAME: "随便社区",
          EVENT_SRC_NAME: "12345",
          SUB_TYPE_NAME: "事发时是",
          EVENT_PROPERTY_NAME: "投诉",
          DISPOSE_UNIT_NAME: "龙田街道综合执法队"
        },
        {
          CREATE_TIME: "2018-07-04 17:24:41",
          STREET_NAME: "龙田街道",
          COMMUNITY_NAME: "南布社区",
          EVENT_SRC_NAME: "12345",
          SUB_TYPE_NAME: "市容环卫",
          EVENT_PROPERTY_NAME: "投诉",
          DISPOSE_UNIT_NAME: "龙田街道综合执法队"
        }
      ]
    };
  },
  created: function() {
    var that = this;
    axios
      .post("http://localhost:5000/abnormal", {})
      .then(function(response) {
        console.log(response);
        var a = response.data.result;
        that.marqueeList = a;
        that.animate = false;
        debugger;
      })
      .catch(function(error) {
        console.log(error);
      });
    setInterval(this.showMarquee, 5000);
  },
  mounted() {
  },
  methods: {
    showMarquee: function() {
      this.animate = true;

      setTimeout(() => {
        this.marqueeList.push(this.marqueeList[0]);
        this.marqueeList.shift();
        this.animate = false;
      }, 500);
    }
  }
};
</script>
<style>
div,
ul,
li,
span,
img {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.marquee1 {
  width: 100%;
  height: 30px;
  align-items: center;
  color: #3a3a3a;
  background-color: #b3effe;
  display: flex;
  box-sizing: border-box;
}

.marquee_title1 {
  padding: 0 20px;
  height: 30px;
  font-size: 14px;
  border-right: 3px solid #d8d8d8;
  align-items: center;
}

.marquee_box1 {
  display: block;
  position: relative;
  width: 60%;
  height: 30px;
  overflow: hidden;
}

.marquee_list1 {
  display: block;
  position: absolute;
  overflow: hidden;
  top: 0;
  left: 0;
}

.marquee_top1 {
  transition: all 0.5s;
  margin-top: -30px;
}

.marquee_list1 li {
  height: 30px;
  line-height: 30px;
  font-size: 14px;
  padding-left: 20px;
}

.marquee_list1 li span {
  padding: 0 2px;
}

.red {
  color: #ff0101;
}
</style>
