<template>
  <div class="content">
    <div class="container-fluid">
      <div class="main_page"  v-if="login_state === 'login_user'">
        <div style="padding-bottom:30px">
          <mu-button v-on:click="add_a_tab"> 
            <mu-icon left size="30" value="library_add"></mu-icon>
          </mu-button>
        </div>
        <mu-container>
          <mu-tabs :value.sync="graphic_active">
            <mu-tab v-for="graphic in graphic_selection" v-bind:key="graphic.id">
              {{ graphic.name }}
            </mu-tab>
          </mu-tabs>
          <div class="tab_page" v-show="graphic_active === i"
          v-for="(graphic,i) in graphic_selection" v-bind:key="graphic.id"
         >
            <mu-row>
              <mu-alert color="warning" @delete="alert1 = false" delete v-if="alert1" transition="mu-scale-transition">
                <mu-icon left value="warning"></mu-icon> 没有选择分析类型
              </mu-alert>
            </mu-row>
            <mu-row class="grahpic_selection">
              <mu-col span="2">
                <mu-menu
                  placement="top-start"
                  open-on-hover
                  style="padding-top:25px"
                  id="graphic"
                >
                  <mu-button color="blue">图表类型</mu-button>
                  <mu-list slot="content">
                    <mu-list-item
                      button
                      v-on:click="set_graphic_type(item.name)"
                      v-for="(item, index) in aspect"
                      :key="index"
                    >
                      <mu-list-item-title>{{ item.name }}</mu-list-item-title>
                    </mu-list-item>
                  </mu-list>
                </mu-menu>
              </mu-col>
              <mu-col span="4">
                <mu-date-input
                  actions 
                  icon="today"
                  :max-date="maxDate" 
                  :min-date="minDate"
                  v-model="selected_start_date"
                  label="选择开始日期"
                  type="date"
                  label-float
                  full-width
                ></mu-date-input>
                <!-- action用来确定取消 -->
              </mu-col>
               <mu-col span="4">
                <mu-date-input
                  icon="today"
                  v-model="selected_end_date"
                  label="选择结束日期"
                  type="date"
                  label-float
                  full-width
                ></mu-date-input>
              </mu-col> 
              <mu-col span="2">
                <div style="padding-top:25px; padding-left:20px">
                  <mu-button v-on:click="set_graphic">确定生成</mu-button>
                  <mu-button v-on:click="see">查看</mu-button>
                </div>
              </mu-col>
            </mu-row>
            
            <div :id="set_graphic_id(i)">
              <graphic-pic ref = "drawline"></graphic-pic>
              <!-- <street-event></street-event> -->
            </div>
            <!-- <street-event></street-event> -->
          </div>
        </mu-container>
      </div>
      <div class="main_page" v-if="login_state === 'traveler'">
        请登录
      </div>
    </div>
  </div>
</template>
<script>
import { type } from "os";
import axios from "axios";
import GraphicPic from "src/pages/GraphicPic.vue";
import StreetEvent from "src/pages/StreetEvent.vue";
export default {
  components: {
    GraphicPic,
    StreetEvent
  },
  data() {
    const minDate = new Date();
    const maxDate = new Date();
    const normalDate = new Date();
    minDate.setFullYear(2018);
    minDate.setMonth(5);
    minDate.setDate(1);
    maxDate.setFullYear(2018);
    maxDate.setMonth(10);
    maxDate.setDate(6);
    normalDate.setFullYear(2018);
    normalDate.setMonth(9);
    normalDate.setDate(1);
      // 设置日期范围
    return {
      alert1:false,
      minDate,
      maxDate,
      login_state:"",
      url:"C:/develop/code/html/GovDataStation/src/pages/hot_community.html",
      graphic_num: 0,
      graphic_active: 0,
      graphic_selection: [{name: "请选择图表", type: "", date_start: "", date_end:"" }],
      graphic_dig: [],
      aspect: [
        { name: "反馈统计" },
        { name: "社区事件统计" },
        { name: "热点社区" },
        { name: "事件及处理" }
      ],
      selected_start_date: normalDate,
      selected_end_date: normalDate,
      today: {
        year: 2018,
        month: 10,
        day: 30
      },
      tomorrow: {
        year: 2018,
        month: 10,
        day: 31
      },
      ifshowg:[0]
      
    };
  },
  mounted() {
    this.login_state = sessionStorage["identification"]
    sessionStorage.setItem("graphic_NO",this.graphic_num)
    sessionStorage.setItem("ifshowg",this.ifshowg)
  },
  methods: {
    set_graphic_type(type) {
      this.graphic_selection[this.graphic_active]["type"] = type;
      this.graphic_selection[this.graphic_active]["name"] = type;
    },
    set_graphic() {
      debugger
      if(this.graphic_selection[this.graphic_active]["type"] == ""){
        this.alert1 = true;
      }
      else{
        this.alert1 = false;
      }
      this.graphic_selection[this.graphic_active]["date_start"] = {};
      this.graphic_selection[this.graphic_active]["date_end"] = {};
      if (this.selected_start_date != undefined) {
        this.graphic_selection[this.graphic_active]["date_start"]["year"] =
          this.selected_start_date.getYear() + 1900;
        this.graphic_selection[this.graphic_active]["date_start"]["month"] =
          this.selected_start_date.getMonth() + 1;
        this.graphic_selection[this.graphic_active]["date_start"]["day"] = 
          this.selected_start_date.getDate();
      } else this.graphic_selection[this.graphic_active]["date_start"] = this.today;
      if (this.selected_end_date != undefined) {
        this.graphic_selection[this.graphic_active]["date_end"]["year"] =
          this.selected_end_date.getYear() + 1900;
        this.graphic_selection[this.graphic_active]["date_end"]["month"] =
          this.selected_end_date.getMonth() + 1;
        this.graphic_selection[this.graphic_active]["date_end"]["day"] = 
          this.selected_end_date.getDate();
      } else {
          this.graphic_selection[this.graphic_active]["date_end"] = this.tomorrow;
      }
      debugger
      if (this.graphic_selection[type] === "") {
        aleat("请选择图表类型");
      } else this.get_graphic(this.graphic_selection[this.graphic_active]);
    },
    get_graphic(graphic_selection) {
      var that = this
      axios
        .post("http://localhost:5000/chartfunction", {
          graphic_selection
        })
        .then(function(response) {
          console.log(response);
          var a = response.data.result
          that.graphic_dig[that.graphic_active] = a
          that.ifshowg[that.graphic_active] = 1
          sessionStorage.setItem("graphic",JSON.stringify(that.graphic_dig))
          sessionStorage.setItem("graphic_selection",JSON.stringify(that.graphic_selection))
          sessionStorage.setItem("ifshowg",that.ifshowg)
          that.$refs.drawline[that.graphic_active].drawLine(that.graphic_num)
        })
        .catch(function(error) {
          console.log(error);
        });
        // sessionStorage.setItem("graphic",this.StreetEvents)
    },
    get_graphic_test(graphic_selection) {
        this.graphic_dig[this.graphic_active] = this.event_deals
        sessionStorage.setItem("graphic",JSON.stringify(this.graphic_dig))
        sessionStorage.setItem("graphic_selection",JSON.stringify(this.graphic_selection))
    },
    see() {
      sessionStorage.setItem("graphic",JSON.stringify(this.graphic_dig))
      debugger
    },
    add_a_tab(){
      this.graphic_num += 1
      this.graphic_selection.push({ name: "请选择图表", type: "", date_start: "", date_end:"" })
      this.ifshowg.push(0)
      sessionStorage.setItem("ifshowg",JSON.stringify(this.ifshowg))
      sessionStorage.setItem("graphic",JSON.stringify(this.graphic_dig))
      sessionStorage.setItem("graphic_NO",this.graphic_num)
      sessionStorage.setItem("graphic_selection",JSON.stringify(this.graphic_selection))
    },
    set_graphic_id(i){
      return "graphic_" + i
    },
    set_ref(i){
      return i
    }
  }
};
</script>
<style>
.tab_page {
  padding: 16px;
  background: #fff;
  margin: 8px 0;
}
.graphic_selection {
  vertical-align: middle;
}
</style>
