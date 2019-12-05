<template>
  <div class="content">
    <div class="container-fluid">
      <div v-if="if_user == true">
        <div style="text-align:center; padding-bottom:40px">
          请输入要查找的数据库信息
        </div>
        <mu-button v-on:click="search">
          Search
          <mu-icon right value="search"></mu-icon>
        </mu-button>
        <mu-container>
          <mu-flex align-items="center" style="padding-bottom: 8px;"> </mu-flex>
          <mu-form
            :model="form"
            class="mu-demo-form"
            :label-position="labelPosition"
            label-width="100"
          >
            <mu-row>
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
            <mu-row>
              <mu-form-item prop="select" label="所属区域">
                <mu-select v-model="form['DISTRICT_NAME']">
                  <mu-option
                    v-for="option in dict['DISTRICT_NAME']"
                    :key="option"
                    :label="option"
                    :value="option"
                  ></mu-option>
                </mu-select>
              </mu-form-item>
              <mu-form-item prop="select" label="所属街道">
                <mu-select v-model="form['STREET_NAME']">
                  <mu-option
                    v-for="option in dict['STREET_NAME']"
                    :key="option"
                    :label="option"
                    :value="option"
                  ></mu-option>
                </mu-select>
              </mu-form-item>
              <mu-form-item prop="select" label="所属社区">
                <mu-select v-model="form['COMMUNITY_NAME']">
                  <mu-option
                    v-for="option in dict['COMMUNITY_NAME']"
                    :key="option"
                    :label="option"
                    :value="option"
                  ></mu-option>
                </mu-select>
              </mu-form-item>
            </mu-row>
            <mu-row>
              <mu-col span="3">
                <mu-form-item prop="select" label="事件类型">
                  <mu-select v-model="form['EVENT_TYPE_NAME']">
                    <mu-option
                      v-for="option in dict['EVENT_TYPE_NAME']"
                      :key="option"
                      :label="option"
                      :value="option"
                    ></mu-option>
                  </mu-select>
                </mu-form-item>
              </mu-col>
            </mu-row>

            <mu-row>
              <mu-col span="6">
                <mu-form-item prop="input" label="大类名称">
                  <mu-text-field
                    v-model="form['MAIN_TYPE_NAME']"
                  ></mu-text-field> </mu-form-item
              ></mu-col>
              <mu-col span="6">
                <mu-form-item prop="input" label="小类名称">
                  <mu-text-field
                    v-model="form['SUB_TYPE_NAME']"
                  ></mu-text-field> </mu-form-item
              ></mu-col>
            </mu-row>
            <mu-row>
              <mu-col span="6 ">
                <mu-form-item prop="input" label="处置部门">
                  <mu-text-field
                    v-model="form['DISPOSE_UNIT_NAME']"
                  ></mu-text-field>
                </mu-form-item>
              </mu-col>
            </mu-row>

            <mu-row>
              <mu-form-item prop="select" label="问题来源">
                <mu-select v-model="form['EVENT_SRC_NAME']">
                  <mu-option
                    v-for="option in dict['EVENT_SRC_NAME']"
                    :key="option"
                    :label="option"
                    :value="option"
                  ></mu-option>
                </mu-select>
              </mu-form-item>
              <mu-form-item prop="select" label="问题结办情况">
                <mu-select v-model="solve_result">
                  <mu-option
                    v-for="option in dict['问题结办情况']"
                    :key="option"
                    :label="option"
                    :value="option"
                  ></mu-option>
                </mu-select>
              </mu-form-item>
              <mu-form-item prop="select" label="问题性质">
                <mu-select v-model="form['EVENT_PROPERTY_NAME']">
                  <mu-option
                    v-for="option in dict['EVENT_PROPERTY_NAME']"
                    :key="option"
                    :label="option"
                    :value="option"
                  ></mu-option>
                </mu-select>
              </mu-form-item>
            </mu-row>
          </mu-form>
        </mu-container>
        <mu-container>
          <mu-paper :z-depth="1">
            <mu-data-table
              height="300"
              :columns="columns"
              :sort.sync="sort"
              @sort-change="handleSortChange"
              :data="list"
            >
              <template slot-scope="scope">
                <td class="is-right">{{ scope.row.time }}</td>
                <td class="is-right">{{ scope.row.district }}</td>
                <td class="is-right">{{ scope.row.street }}</td>
                <td class="is-right">{{ scope.row.community }}</td>
                <td class="is-right">{{ scope.row.type }}</td>
                <td class="is-right">{{ scope.row.main_type }}</td>
                <td class="is-right">{{ scope.row.sub_type }}</td>
                <td class="is-right">{{ scope.row.unit }}</td>
                <td class="is-right">{{ scope.row.src }}</td>
                <td class="is-right">{{ scope.row.solved }}</td>
                <td class="is-right">{{ scope.row.property }}</td>
              </template>
            </mu-data-table>
          </mu-paper>
        </mu-container>
      </div>
      <div v-if="if_user != true">
        请登录
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    const normalDate = new Date();
    normalDate.setFullYear(2018);
    normalDate.setMonth(9);
    normalDate.setDate(1);
    return {
      if_user:false,
      dict: {
        DISTRICT_NAME: ["坪山区"],
        STREET_NAME: [
          "龙田街道",
          "坪山街道",
          "碧岭街道",
          "坑梓街道",
          "马峦街道",
          "石井街道"
        ],
        COMMUNITY_NAME: [
          "老坑社区",
          "六和社区",
          "沙湖社区",
          "六联社区",
          "金沙社区",
          "秀新社区",
          "坑梓社区",
          "坪环社区",
          "和平社区",
          "坪山社区",
          "龙田社区",
          "沙田社区",
          "石井社区",
          "南布社区",
          "沙坣社区",
          "金龟社区",
          "碧岭社区",
          "竹坑社区",
          "江岭社区",
          "汤坑社区",
          "田头社区",
          "田心社区",
          "马峦社区"
        ],
        EVENT_TYPE_NAME: [
          "市政设施",
          "市容环卫",
          "环保水务",
          "教育卫生",
          "规土城建",
          "食药市监",
          "交通运输",
          "安全隐患",
          "社区管理",
          "民政服务",
          "治安维稳",
          "党纪政纪",
          "劳动社保",
          "专业事件采集",
          "组织人事",
          "统一战线",
          "党建群团",
          "文体旅游"
        ],
        EVENT_SRC_NAME: [
          "@坪山",
          "12319",
          "政府信箱",
          "美丽深圳",
          "固话投诉",
          "12345"
        ],
        问题结办情况: ["超期结办", "处置中", "按期结办"],
        EVENT_PROPERTY_NAME: ["投诉", "感谢", "咨询", "建议", "求决", "其他"]
      },
      solve_result: "",
      form: {
        DISTRICT_NAME: "",
        STREET_NAME: "",
        COMMUNITY_NAME: "",
        EVENT_TYPE_NAME: "",
        EVENT_SRC_NAME: "",
        MAIN_TYPE_NAME: "",
        SUB_TYPE_NAME: "",
        DISPOSE_UNIT_NAME: "",
        OVERTIME_ARCHIVE_NUM: 1,
        INTIME_TO_ARCHIVE_NUM: 0,
        INTIME_ARCHIVE_NUM: 0,
        EVENT_PROPERTY_NAME: ""
      },
      start_time: {
        year: "",
        month: "",
        day: ""
      },
      end_time: {
        year: "",
        month: "",
        day: ""
      },
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
      sort: {
        name: "",
        order: "asc"
      },
      columns: [
        { title: "统计时间", width: 200, name: "time" },
        {
          title: "所属区域",
          name: "district",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "所属街道",
          name: "street",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "所属社区",
          name: "community",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "事件类型",
          name: "type",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "大类名称",
          name: "main_type",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "小类名称",
          name: "sub_type",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "处置部门",
          name: "unit",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "问题来源",
          name: "src",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "问题结办情况",
          name: "solved",
          width: 126,
          align: "center",
          sortable: true
        },
        {
          title: "问题性质",
          name: "property",
          width: 126,
          align: "center",
          sortable: true
        }
      ],
      list: []
    };
  },
  mounted(){
    if(sessionStorage["identification"] == "login_user"){
      this.if_user = true
    }
    if(sessionStorage["identification"] == "Admin"){
      this.if_user = true
    }
  },
  methods: {
    handleSortChange({ name, order }) {
      this.list = this.list.sort((a, b) =>
        order === "asc" ? a[name] - b[name] : b[name] - a[name]
      );
    },
    get_time() {
      debugger;
      this.start_time["year"] = this.selected_start_date.getYear() + 1900;
      this.start_time["month"] = this.selected_start_date.getMonth() + 1;
      this.start_time["day"] = this.selected_start_date.getDate();

      this.end_time["year"] = this.selected_end_date.getYear() + 1900;
      this.end_time["month"] = this.selected_end_date.getMonth() + 1;
      this.end_time["day"] = this.selected_end_date.getDate();
    },
    search() {
      if (this.solve_result == "超期结办") {
        this.form[OVERTIME_ARCHIVE_NUM] = 1;
        this.form[INTIME_TO_ARCHIVE_NUM] = 0;
        this.form[INTIME_ARCHIVE_NUM] = 0;
      } else if (this.solve_result == "处置中") {
        this.form[OVERTIME_ARCHIVE_NUM] = 0;
        this.form[INTIME_TO_ARCHIVE_NUM] = 1;
        this.form[INTIME_ARCHIVE_NUM] = 0;
      } else if (this.solve_result == "按期结办") {
        this.form[OVERTIME_ARCHIVE_NUM] = 0;
        this.form[INTIME_TO_ARCHIVE_NUM] = 0;
        this.form[INTIME_ARCHIVE_NUM] = 1;
      }
      this.get_time();
      var that = this;
      var values = this.form;
      var start_time = this.start_time;
      var end_time = this.end_time;
      axios
        .post("http://localhost:5000/search", {
          start_time,
          end_time,
          values
        })
        .then(function(response) {
          that.list = [];
          var result = response["data"]["result"];
          debugger;
          for (var i = 0; i < result.length; i++) {
            var a_log = {
              time: "",
              district: "",
              street: "",
              community: "",
              type: "",
              main_type: "",
              sub_type: "",
              unit: "",
              src: "",
              solved: "",
              property: ""
            };
            a_log["time"] = result[i][2];
            a_log["district"] = result[i][3];
            a_log["street"] = result[i][5];
            a_log["community"] = result[i][7];
            a_log["type"] = result[i][9];
            a_log["main_type"] = result[i][11];
            a_log["sub_type"] = result[i][13];
            a_log["unit"] = result[i][15];
            a_log["src"] = result[i][17];
            if (result[i][20] == 1) {
              a_log["solved"] = "超期结办";
            } else if (result[i][20] == 1) {
              a_log["solved"] = "处置中";
            } else {
              a_log["solved"] = "按期结办";
            }
            a_log["property"] = result[i][24];
            that.list.push(a_log);
          }
          debugger;
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style></style>
