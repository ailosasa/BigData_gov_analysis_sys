<template>
  <section>
    <div class="home_siderbar">
      <mu-list height=100%>
        <mu-list-item>
          <mu-button icon
                     color="primary">
            <mu-icon value="grade"></mu-icon>
          </mu-button>
        </mu-list-item>
        <mu-list-item>
          <mu-button :secondary="true"
                     :fullWidth="true"
                     v-on:click="ToLoginPage">1.用户
          </mu-button>
        </mu-list-item>
        <mu-list-item>
          <mu-button :secondary="true"
                     :fullWidth="true"
                     v-on:click="ToDatasetPage">2.查看数据
          </mu-button>
        </mu-list-item>
        <mu-list-item>
          <mu-button :secondary="true"
                     :fullWidth="true"
                     v-on:click="ToAnalysisPage">3.大数据分析
          </mu-button>
        </mu-list-item>
      </mu-list>
    </div>

    <div class="homepage"
         v-if="home_page_num === 0 ">
      <!-- 先用0来表示，后面要替换成login标签 -->

      <div class="login_page">
        <img src="./assets/home_trade_marker.png"
             width="100%"
             class="home_img">
        <div class="input-area">
          <mu-icon size="60"
                   value="people"></mu-icon>
          <div><input type="text"
                   class="qxs-ic_user qxs-icon"
                   placeholder="用户名"
                   v-model="userName">
          </div>
          <div>
            <input type="text"
                   class="qxs-ic_password qxs-icon"
                   placeholder="密码"
                   v-model="password"></div>
          <div><button v-on:click="login">登陆</button></div>
        </div>
      </div>

      <mu-bottom-nav class="down_leader">
        <mu-bottom-nav-item title="treaty">协议</mu-bottom-nav-item>
        <mu-bottom-nav-item title="privaty">隐私</mu-bottom-nav-item>
        <mu-bottom-nav-item title="help">帮助</mu-bottom-nav-item>
      </mu-bottom-nav>
    </div>
    <div class="homepage"
         v-if="home_page_num === 1">
      <div class="choose_page">
        请选择希望查询的项目

        <div class="choose_page">
          <mu-row>
            <mu-col span="6">
              项目类型
            </mu-col>
            <mu-col span="6">
              <mu-menu placement="top-start"
                       open-on-hover>
                <mu-button color="blue">请选择项目类型</mu-button>
                <mu-list slot="content">
                  <mu-list-item v-for="(item,index) in aspect"
                                :key='index'>
                    <mu-button>{{item.name}}</mu-button>
                  </mu-list-item>
                </mu-list>
              </mu-menu>
            </mu-col>
          </mu-row>
        </div>
        <div class="choose_page">
          <mu-row>
            <mu-col span="6">
              区
            </mu-col>
            <mu-col span="6">
              <mu-menu placement="top-start"
                       open-on-hover>
                <mu-button color="blue">请选择项目类型</mu-button>
                <mu-list slot="content">
                  <mu-list-item v-for="(item,index) in aspect"
                                :key='index'>
                    <mu-button>{{item.name}}</mu-button>
                  </mu-list-item>
                </mu-list>
              </mu-menu>
            </mu-col>
          </mu-row>
        </div>
        <div class="choose_page">
          <mu-row>
            <mu-col span="6">
              街道
            </mu-col>
            <mu-col span="6">
              <mu-menu placement="top-start"
                       open-on-hover>
                <mu-button color="blue">请选择项目类型</mu-button>
                <mu-list slot="content">
                  <mu-list-item v-for="(item,index) in aspect"
                                :key='index'>
                    <mu-button>{{item.name}}</mu-button>
                  </mu-list-item>
                </mu-list>
              </mu-menu>
            </mu-col>
          </mu-row>
        </div>
        <div class="choose_page">
          <mu-row>
            <mu-col span="6">
              社区
            </mu-col>
            <mu-col span="6">
              <mu-menu placement="top-start"
                       open-on-hover>
                <mu-button color="blue">请选择项目类型</mu-button>
                <mu-list slot="content">
                  <mu-list-item v-for="(item,index) in aspect"
                                :key='index'>
                    <mu-button>{{item.name}}</mu-button>
                  </mu-list-item>
                </mu-list>
              </mu-menu>
            </mu-col>
          </mu-row>
        </div>
        <div class="choose_page">
          <mu-row>
            <mu-col span="6">
              相关部门
            </mu-col>
            <mu-col span="6">
              <mu-menu placement="top-start"
                       open-on-hover>
                <mu-button color="blue">请选择项目类型</mu-button>
                <mu-list slot="content">
                  <mu-list-item v-for="(item,index) in aspect"
                                :key='index'>
                    <mu-button>{{item.name}}</mu-button>
                  </mu-list-item>
                </mu-list>
              </mu-menu>
            </mu-col>
          </mu-row>
        </div>
        <div class="choose_page">
          <mu-row>
            <mu-col span="6">
              投诉类型
            </mu-col>
            <mu-col span="6">
              <mu-menu placement="top-start"
                       open-on-hover>
                <mu-button color="blue">请选择项目类型</mu-button>
                <mu-list slot="content">
                  <mu-list-item v-for="(item,index) in aspect"
                                :key='index'>
                    <mu-button>{{item.name}}</mu-button>
                  </mu-list-item>
                </mu-list>
              </mu-menu>
            </mu-col>
          </mu-row>
        </div>
      </div>
      <mu-paper :z-depth="1">
        <mu-data-table :columns="columns"
                       :sort.sync="sort"
                       @sort-change="handleSortChange"
                       :data="list">
          <template slot-scope="scope">
            <td>{{scope.row.name}}</td>
            <td class="is-right">{{scope.row.calories}}</td>
            <td class="is-right">{{scope.row.fat}}</td>
            <td class="is-right">{{scope.row.carbs}}</td>
            <td class="is-right">{{scope.row.protein}}</td>
            <td class="is-right">{{scope.row.iron}}%</td>
          </template>
        </mu-data-table>
      </mu-paper>
    </div>
    <div class="homepage"
         v-if="home_page_num === 2">
      <div class="TabPage">
        <mu-tabs>
          <mu-tab v-for="(item,index) in AnalysisGragh"
                  :key="index">{{item.name}}</mu-tab>
        </mu-tabs>
      </div>
      <div class=""
           v-if="AnalysisG_num === 0">
        <mu-carousel>
          <mu-carousel-item>
            <div id="myChart"
                 :style="{width: '300px', height: '300px'}"></div>
          </mu-carousel-item>
          <mu-carousel-item>
            <img src="./assets/logo.png">
          </mu-carousel-item>
        </mu-carousel>
      </div>

    </div>
  </section>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      docked: false,
      open: true,
      position: 'left',
      aspect: [{ name: 'shirong' }, { name: 'zhixu' }],
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        { title: 'Dessert (100g serving)', width: 200, name: 'name' },
        {
          title: 'Calories',
          name: 'calories',
          width: 126,
          align: 'center',
          sortable: true
        },
        {
          title: 'Fat (g)',
          name: 'fat',
          width: 126,
          align: 'center',
          sortable: true
        },
        {
          title: 'Carbs (g)',
          name: 'carbs',
          width: 126,
          align: 'center',
          sortable: true
        },
        {
          title: 'Protein (g)',
          name: 'protein',
          width: 126,
          align: 'center',
          sortable: true
        },
        {
          title: 'Iron (%)',
          name: 'iron',
          width: 126,
          align: 'center',
          sortable: true
        }
      ],
      list: [
        {
          name: 'Frozen Yogurt',
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: 1
        },
        {
          name: 'Ice cream sandwich',
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: 1
        },
        {
          name: 'Eclair',
          calories: 262,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: 7
        },
        {
          name: 'Cupcake',
          calories: 305,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: 8
        },
        {
          name: 'Gingerbread',
          calories: 356,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: 16
        },
        {
          name: 'Jelly bean',
          calories: 375,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: 0
        },
        {
          name: 'Lollipop',
          calories: 392,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: 2
        },
        {
          name: 'Honeycomb',
          calories: 408,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: 45
        },
        {
          name: 'Donut',
          calories: 452,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: 22
        },
        {
          name: 'KitKat',
          calories: 518,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: 6
        }
      ],
      AnalysisGragh: [{ name: '图表主页' }, { name: '今日热度区域' }, { name: '近日诉求变化' }],
      home_page_num: 2,
      AnalysisG_num: 0
    }
  },
  mounted () {
    this.drawLine()
  },
  methods: {
    ToLoginPage () {
      this.home_page_num = 0
    },
    ToDatasetPage () {
      this.home_page_num = 1
    },
    ToAnalysisPage () {
      this.home_page_num = 2
    },
    drawLine () {
      // 基于准备好的dom，初始化echarts实例
      let myChart = this.$echarts.init(document.getElementById('myChart'))
      // 绘制图表
      myChart.setOption({
        title: { text: '在Vue中使用echarts' },
        tooltip: {},
        xAxis: {
          data: ['乱摆乱放', '乱摆乱放', '乱摆乱放', '乱摆乱放', '乱摆乱放', '乱摆乱放']
        },
        yAxis: {},
        series: [{
          name: '数目',
          type: 'bar',
          data: [5, 20, 36, 10, 10, 20]
        }]
      })
    }
  }
}
</script>

<style>
@import "https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css";
@import "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic";

.home_siderbar {
  background-color: #3622e6;
  float: left;
  width: 150px;
  /* height: calc(100vh - 300px); */
  height: 1000px;
  position: fixed;
}
.homepage {
  /* float: right; */
  position: absolute;
  left: 150px;
  right: 0px;
  height: 1000px;
}
.home_topbar {
  background-color: #3622e6;
  width: 100%;
  color: yellow;
}
.login_page {
  padding-top: 20%;
  padding-left: 0%;
  padding-right: 10%;
  text-align: center;
}
.home_img {
  padding-bottom: 50px;
}
.login_form {
  padding-top: 0%;
  padding-left: 10%;
  padding-right: 10%;
  text-align: center;
}
.input-area input {
  width: 200px;
  height: 40px;
  line-height: 20px;
  margin: 10px 0;
  outline: none;
  border: 1px solid rgba(209, 204, 204, 0.897);
}
.input-area button {
  width: 200px;
  height: 40px;
  line-height: 20px;
  background-color: #3622e6;
  border: none;
  margin: 10px 0;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
}
.down_leader {
  position: fixed;
  bottom: 0;
}
.choose_page {
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 0%;
}
.TabPage {
  padding-left: 0%;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
