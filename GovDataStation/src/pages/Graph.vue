<template>
  <div class="content">
    <div class="container-fluid">
      <div class="main_page" v-if="if_user === true" ref="screen_cut">
        <div style="padding-bottom:30px">
          <mu-button v-on:click="add_a_tab">
            <mu-icon left size="30" value="library_add"></mu-icon>
          </mu-button>
        </div>
        <mu-container>
          <mu-tabs :value.sync="graphic_active">
            <mu-tab
              v-for="graphic in graphic_selection"
              v-bind:key="graphic.id"
            >
              {{ graphic.name }}
            </mu-tab>
          </mu-tabs>
          <div
            class="tab_page"
            v-show="graphic_active === i"
            v-for="(graphic, i) in graphic_selection"
            v-bind:key="graphic.id"
          >
            <mu-row style="padding-bottom:10px">
              <mu-col span="2">
                <mu-icon
                  size="30"
                  value="cloud_download"
                  v-on:click="pic_dowmload"
                  color="orange"
                ></mu-icon>
              </mu-col>
              <mu-col span="9"></mu-col>
              <mu-col span="1">
                <mu-icon value="clear" v-on:click="delete_page" right></mu-icon>
              </mu-col>
            </mu-row>

            <mu-row>
              <mu-alert
                color="warning"
                @delete="alert1 = false"
                delete
                v-if="alert1"
                transition="mu-scale-transition"
              >
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
            </mu-row>

            <div :id="set_graphic_id(i)" style="width:900px; height:500px">
              <graphic-pic ref="drawline"></graphic-pic>
              <!-- <street-event></street-event> -->
            </div>
            <!-- <street-event></street-event> -->
          </div>
        </mu-container>
      </div>
      <div class="main_page" v-if="if_user != true">
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
import html2canvas from "html2canvas";

export default {
  components: {
    GraphicPic,
    StreetEvent
  },
  data() {
    const minDate = new Date();
    const maxDate = new Date();

    minDate.setFullYear(2018);
    minDate.setMonth(5);
    minDate.setDate(1);
    maxDate.setFullYear(2018);
    maxDate.setMonth(10);
    maxDate.setDate(6);
    const normalDate = new Date();
    normalDate.setFullYear(2018);
    normalDate.setMonth(9);
    normalDate.setDate(30);
    // 设置日期范围
    return {
      alert1: false,
      minDate,
      maxDate,
      if_user: false,
      url: "C:/develop/code/html/GovDataStation/src/pages/hot_community.html",
      graphic_num: 0,
      graphic_active: 0,
      graphic_selection: [
        { name: "请选择图表", type: "反馈统计", date_start: "", date_end: "" }
      ],
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
      ifshowg: [0]
    };
  },
  mounted() {
    if (sessionStorage["identification"] == "login_user") {
      this.if_user = true;
    }
    if (sessionStorage["identification"] == "Admin") {
      this.if_user = true;
    }
    sessionStorage.setItem("graphic_NO", this.graphic_num);
    sessionStorage.setItem("ifshowg", this.ifshowg);
    debugger;
    this.set_graphic();
  },
  methods: {
    set_graphic_type(type) {
      this.graphic_selection[this.graphic_active]["type"] = type;
      this.graphic_selection[this.graphic_active]["name"] = type;
      this.set_graphic();
      setInterval(this.update_pic, 5000);
    },
    set_graphic() {
      if (this.graphic_selection[this.graphic_active]["type"] == "") {
        this.alert1 = true;
      } else {
        this.alert1 = false;
      }
      this.graphic_selection[this.graphic_active]["date_start"] = {};
      this.graphic_selection[this.graphic_active]["date_end"] = {};
      if (this.selected_start_date != undefined) {
        this.graphic_selection[this.graphic_active]["date_start"]["year"] =
          this.selected_start_date.getYear() + 1900;
        this.graphic_selection[this.graphic_active]["date_start"]["month"] =
          this.selected_start_date.getMonth() + 1;
        this.graphic_selection[this.graphic_active]["date_start"][
          "day"
        ] = this.selected_start_date.getDate();
      } else
        this.graphic_selection[this.graphic_active]["date_start"] = this.today;
      if (this.selected_end_date != undefined) {
        this.graphic_selection[this.graphic_active]["date_end"]["year"] =
          this.selected_end_date.getYear() + 1900;
        this.graphic_selection[this.graphic_active]["date_end"]["month"] =
          this.selected_end_date.getMonth() + 1;
        this.graphic_selection[this.graphic_active]["date_end"][
          "day"
        ] = this.selected_end_date.getDate();
      } else {
        this.graphic_selection[this.graphic_active]["date_end"] = this.tomorrow;
      }
      if (this.graphic_selection[type] === "") {
        aleat("请选择图表类型");
      } else this.get_graphic(this.graphic_selection[this.graphic_active]);
    },
    get_graphic(graphic_selection) {
      var that = this;
      axios
        .post("http://localhost:5000/chartfunction", {
          graphic_selection
        })
        .then(function(response) {
          console.log(response);

          that.graphic_dig[that.graphic_active] = response.data.result;
          that.ifshowg[that.graphic_active] = 1;
          sessionStorage.setItem("graphic", JSON.stringify(that.graphic_dig));
          sessionStorage.setItem(
            "graphic_selection",
            JSON.stringify(that.graphic_selection)
          );
          sessionStorage.setItem("ifshowg", that.ifshowg);
          debugger;
          that.$refs.drawline[that.graphic_active].drawLine(
            that.graphic_active
          );
        })
        .catch(function(error) {
          console.log(error);
        });
      // sessionStorage.setItem("graphic",this.StreetEvents)
    },
    get_graphic_test(graphic_selection) {
      this.graphic_dig[this.graphic_active] = this.event_deals;
      sessionStorage.setItem("graphic", JSON.stringify(this.graphic_dig));
      sessionStorage.setItem(
        "graphic_selection",
        JSON.stringify(this.graphic_selection)
      );
    },
    update_pic() {
      debugger;
      if (this.if_user == true) {
        if (this.graphic_selection[this.graphic_active]["type"] == "") {
          this.alert1 = true;
        } else {
          this.alert1 = false;
        }
        this.graphic_selection[this.graphic_active]["date_start"] = {};
        this.graphic_selection[this.graphic_active]["date_end"] = {};
        if (this.selected_start_date != undefined) {
          this.graphic_selection[this.graphic_active]["date_start"]["year"] =
            this.selected_start_date.getYear() + 1900;
          this.graphic_selection[this.graphic_active]["date_start"]["month"] =
            this.selected_start_date.getMonth() + 1;
          this.graphic_selection[this.graphic_active]["date_start"][
            "day"
          ] = this.selected_start_date.getDate();
        } else
          this.graphic_selection[this.graphic_active][
            "date_start"
          ] = this.today;
        if (this.selected_end_date != undefined) {
          this.graphic_selection[this.graphic_active]["date_end"]["year"] =
            this.selected_end_date.getYear() + 1900;
          this.graphic_selection[this.graphic_active]["date_end"]["month"] =
            this.selected_end_date.getMonth() + 1;
          this.graphic_selection[this.graphic_active]["date_end"][
            "day"
          ] = this.selected_end_date.getDate();
        } else {
          this.graphic_selection[this.graphic_active][
            "date_end"
          ] = this.tomorrow;
        }
        if (this.graphic_selection[type] === "") {
          aleat("请选择图表类型");
        } else {
          var that = this;
          var graphic_selection = this.graphic_selection[this.graphic_active];
          axios
            .post("http://localhost:5000/chartfunction", {
              graphic_selection
            })
            .then(function(response) {
              console.log(response);

              that.graphic_dig[that.graphic_active] = response.data.result;
              that.ifshowg[that.graphic_active] = 1;
              sessionStorage.setItem(
                "graphic",
                JSON.stringify(that.graphic_dig)
              );
              sessionStorage.setItem(
                "graphic_selection",
                JSON.stringify(that.graphic_selection)
              );
              sessionStorage.setItem("ifshowg", that.ifshowg);
              debugger;
              that.$refs.drawline[that.graphic_active].update_pic(
                that.graphic_active
              );
            })
            .catch(function(error) {
              console.log(error);
            });
        }
      }
    },
    pic_dowmload() {
      debugger;
      html2canvas(this.$refs.screen_cut, {
        backgroundColor: null
      }).then(canvas => {
        let dataURL = canvas.toDataURL("image/png");
        this.dataURL = dataURL;
        console.log(dataURL);
        debugger;
        var a = document.createElement("a"); // 生成一个a元素
        var event = new MouseEvent("click"); // 创建一个单击事件
        a.download = name || "photo"; // 设置图片名称
        a.href = dataURL; // 将生成的URL设置为a.href属性
        a.dispatchEvent(event);
      });
    },
    add_a_tab() {
      debugger;
      this.graphic_num += 1;
      this.graphic_selection.push({
        name: "请选择图表",
        type: "",
        date_start: "",
        date_end: ""
      });
      this.ifshowg.push(0);
      sessionStorage.setItem("ifshowg", JSON.stringify(this.ifshowg));
      sessionStorage.setItem("graphic", JSON.stringify(this.graphic_dig));
      sessionStorage.setItem("graphic_NO", this.graphic_num);
      sessionStorage.setItem(
        "graphic_selection",
        JSON.stringify(this.graphic_selection)
      );
      debugger;
    },
    set_graphic_id(i) {
      return "page_" + i;
    },
    set_ref(i) {
      return i;
    },
    delete_page() {
      if (this.graphic_selection.length != 1) {
        this.graphic_selection.pop(this.graphic_active);
      }
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
