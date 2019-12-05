<template>
  <div style="height = 100%">
    <div :id="set_id()" v-show="if_statis"></div>
    <div :id="set_id() + 'pic'">
      <iframe
        :id="set_id() + '_bdPic'"
        src="http://127.0.0.1:8001/hot_community.html"
        frameborder="0"
        width="100%"
        height="100%"
        v-if="if_bdPic"
      ></iframe>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      num: 0,
      if_bdPic: false,
      if_statis: false,
      data: [
        { name: "汤坑社区", value: 100 },
        { name: "坪山社区", value: 200 },
        { name: "南布社区", value: 300 },
        { name: "和平社区", value: 400 },
        { name: "田心社区", value: 500 },
        { name: "金沙社区", value: 600 }
      ],
      geoCoordMap: {
        老坑社区: [114.369312, 22.734866],
        六和社区: [114.349914, 22.707919],
        沙湖社区: [114.326552, 22.67909],
        六联社区: [114.331576, 22.791914],
        金沙社区: [114.406008, 22.75079],
        秀新社区: [114.381223, 22.746873],
        坑梓社区: [114.390013, 22.753031],
        坪环社区: [114.35474, 22.688096],
        和平社区: [114.355104, 22.697106],
        坪山社区: [114.353907, 22.69667],
        龙田社区: [114.372841, 22.753346],
        沙田社区: [114.404444, 22.761764],
        石井社区: [114.390978, 22.697625],
        南布社区: [114.375607, 22.70534],
        沙坣社区: [114.377888, 22.690889],
        金龟社区: [114.406461, 22.663744],
        碧岭社区: [114.295663, 22.67342],
        竹坑社区: [114.395074, 22.715773],
        江岭社区: [114.362596, 22.69202],
        汤坑社区: [114.331079, 22.678805],
        田头社区: [114.410837, 22.697197],
        田心社区: [114.421943, 22.700351],
        马峦社区: [114.338203, 22.644538]
      },
      mychart: ""
    };
  },
  mounted() {},
  methods: {
    drawLine(i) {
      this.if_bdPic = false;
      this.if_statis = false;
      if (sessionStorage["ifshowg"] == 0) return;
      var selection = JSON.parse(sessionStorage["graphic_selection"]);
      var data = JSON.parse(sessionStorage["graphic"]);
      var mychart_id = "graphic_" + i;

      var this_data = data[i];
      var this_selection = selection[i];
      var this_div = document.getElementById(mychart_id);
      this.myChart = this.$echarts.init(this_div);
      // 基于准备好的dom，初始化echarts实例
      if (this_selection["type"] == "反馈统计") {
        this.if_statis = true;
        var option = this.add_date_pie(this_data);
      } else if (this_selection["type"] == "社区事件统计") {
        this.if_statis = true;
        var option = this.add_date_Street(this_data);
      } else if (this_selection["type"] == "热点社区") {
        this.if_bdPic = true;
        document.getElementById(mychart_id + "pic").style.height = "450px";
        document.getElementById(mychart_id + "pic").style.width = "900px";
        this.data = this_data;
        var message = { data: this.data, geoCoordMap: this.geoCoordMap };
        // var id = mychart_id+'_bdpic'
        var myframe = document.getElementById(mychart_id + "_bdPic"); //获取iframe
        myframe.contentWindow.postMessage(
          {
            data: message
          },
          "*"
        );
        return;
      } else {
        this.if_statis = true;
        var option = this.add_date_event(this_data);
      }
      this.myChart = this.$echarts.init(this_div);
      // 准备图表数据
      this.myChart.setOption(option, true);
      debugger;
      document.getElementById(mychart_id).style.height = "450px";
      document.getElementById(mychart_id).style.width = "900px";
      this.myChart.resize();
    },
    update_pic(i) {
      this.if_bdPic = false;
      this.if_statis = false;
      if (sessionStorage["ifshowg"] == 0) return;
      var selection = JSON.parse(sessionStorage["graphic_selection"]);
      var data = JSON.parse(sessionStorage["graphic"]);
      var mychart_id = "graphic_" + i;

      var this_data = data[i];
      var this_selection = selection[i];
      var this_div = document.getElementById(mychart_id);

      // 基于准备好的dom，初始化echarts实例
      if (this_selection["type"] == "反馈统计") {
        this.if_statis = true;
        var option = this.add_date_pie(this_data);
      } else if (this_selection["type"] == "社区事件统计") {
        this.if_statis = true;
        var option = this.add_date_Street(this_data);
      } else if (this_selection["type"] == "热点社区") {
        this.if_bdPic = true;
        document.getElementById(mychart_id + "pic").style.height = "450px";
        document.getElementById(mychart_id + "pic").style.width = "900px";
        this.data = this_data;
        debugger;
        var message = { data: this.data, geoCoordMap: this.geoCoordMap };
        // var id = mychart_id+'_bdpic'
        var myframe = document.getElementById(mychart_id + "_bdPic"); //获取iframe
        myframe.contentWindow.postMessage(
          {
            data: message
          },
          "*"
        );
        return;
      } else {
        this.if_statis = true;
        var option = this.add_date_event(this_data);
      }
      // 准备图表数据
      this.myChart.setOption(option, true);
      debugger;
      document.getElementById(mychart_id).style.height = "450px";
      document.getElementById(mychart_id).style.width = "900px";
      this.myChart.resize();
    },
    add_date_event(EventDeals) {
      var option = {
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b}: {c} ({d}%)"
        },
        legend: {
          orient: "vertical",
          x: "left",
          data: [] // 获取全部的图例
        },
        series: [
          {
            name: "办结情况",
            type: "pie",
            selectedMode: "single",
            radius: [0, "30%"],

            label: {
              normal: {
                position: "inner"
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },
            data: [] // 获取具体办结情况数据
          },
          {
            name: "访问来源",
            type: "pie",
            radius: ["40%", "55%"],
            label: {
              normal: {
                formatter: "{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ",
                backgroundColor: "#eee",
                borderColor: "#aaa",
                borderWidth: 1,
                borderRadius: 4,
                // shadowBlur:3,
                // shadowOffsetX: 2,
                // shadowOffsetY: 2,
                // shadowColor: '#999',
                // padding: [0, 7],
                rich: {
                  a: {
                    color: "#999",
                    lineHeight: 22,
                    align: "center"
                  },
                  // abg: {
                  //     backgroundColor: '#333',
                  //     width: '100%',
                  //     align: 'right',
                  //     height: 22,
                  //     borderRadius: [4, 4, 0, 0]
                  // },
                  hr: {
                    borderColor: "#aaa",
                    width: "100%",
                    borderWidth: 0.5,
                    height: 0
                  },
                  b: {
                    fontSize: 16,
                    lineHeight: 33
                  },
                  per: {
                    color: "#eee",
                    backgroundColor: "#334455",
                    padding: [2, 4],
                    borderRadius: 2
                  }
                }
              }
            },
            data: [] // 获取外层办结情况下事件类型分类的数据
          }
        ]
      }; // 准备图表数据
      for (var name in EventDeals) {
        option.legend.data.push(name);
        for (var l_name in EventDeals[name][1]) {
          option.legend.data.push(l_name);
        }
      }
      for (var deal in EventDeals) {
        // 准备series[1]的数据
        var data = {
          value: EventDeals[deal][0],
          name: deal
        };
        option.series[0].data.push(data);
      }
      for (deal in EventDeals) {
        data = [];
        for (var event in EventDeals[deal][1]) {
          data.push({ value: EventDeals[deal][1][event], name: event });
        }

        if (deal === "超期结办") {
          option.series[1].data = data;
        }
      }
      debugger;
      return option;
    },
    add_date_Street(StreetEvents) {
      var option = {
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: "shadow" // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        legend: {
          data: [] // 需要获取时间类型名
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true
        },
        yAxis: {
          type: "value"
        },
        xAxis: {
          type: "category",
          data: [] // 需要获取展示的街道名
        },
        series: [] // 获取具体数据
      };
      // 下面需要对option进行补充
      var street;
      var event;
      for (street in StreetEvents) {
        // 实现街道名的获取
        option.xAxis.data.push(street);
      }
      for (street in StreetEvents) {
        // 实现事件类型的获取
        for (event in StreetEvents[street]) {
          option.legend.data.push(event);
        }
        break;
      }
      for (var i = 0; i < option.legend.data.length; i++) {
        // 获取具体数据
        var ASerie = {
          name: "",
          type: "bar",
          stack: "总量",
          label: {
            normal: {
              show: true,
              position: "insideRight"
            }
          },
          data: []
        };
        ASerie.name = option.legend.data[i];
        for (street in StreetEvents) {
          ASerie.data.push(StreetEvents[street][ASerie.name]);
        }
        option.series.push(ASerie);
      }
      debugger;
      return option;
    },
    add_date_pie(PieData) {
      var item;
      var dvalue;
      var dname;
      var data = [];
      for (item in PieData) {
        dvalue = PieData[item];
        dname = item;
        var ADate = {};
        ADate["name"] = dname;
        ADate["value"] = dvalue;

        data.push(ADate);
      }

      var option = {
        series: {
          name: "访问来源",
          type: "pie",
          radius: "55%",
          data: data
        }
      };
      return option;
    },
    set_id() {
      var num = sessionStorage["graphic_NO"];
      this.num = num;
      return "graphic_" + num;
    }
  }
};
</script>
