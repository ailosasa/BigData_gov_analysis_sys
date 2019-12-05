<template>
  <div class="content">
    <div class="container-fluid">
      <div class="main_page" v-if="if_admin == true">
        <div style="text-align:center; padding-bottom:40px">
          请输入要查找的数据库信息
        </div>
        <div style="padding-bottom = 50px">
          <mu-button v-on:click="insert_data">
            插入一条信息
            <mu-icon right value="search"></mu-icon>
          </mu-button>
        </div>
        <div>
          <mu-container>
            <mu-flex align-items="center" style="padding-bottom: 8px;">
            </mu-flex>
            <mu-form
              :model="form"
              class="mu-demo-form"
              :label-position="labelPosition"
              label-width="100"
            >
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
        </div>
      </div>
      <div v-if="if_admin != true">
        请以管理员身份登录
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      if_admin:false,
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
        REC_ID: 0,
        REPORT_NUM: "",
        CREATE_TIME: "",
        DISTRICT_NAME: "",
        DISTRICT_ID: "",
        STREET_NAME: "",
        STREET_ID: "",
        COMMUNITY_NAME: "",
        COMMUNITY_ID: "",
        EVENT_TYPE_NAME: "",
        EVENT_TYPE_ID: "",
        MAIN_TYPE_NAME: "",
        MAIN_TYPE_ID: "",
        SUB_TYPE_NAME: "",
        SUB_TYPE_ID: "",
        DISPOSE_UNIT_NAME: "",
        DISPOSE_UNIT_ID: "",
        EVENT_SRC_NAME: "",
        EVENT_SRC_ID: "",
        OPERATE_NUM: "",
        EVENT_PROPERTY_ID: "",
        EVENT_PROPERTY_NAME: "",
        EVENT_PROPERTY_NAME: "",
        OVERTIME_ARCHIVE_NUM: 1,
        INTIME_TO_ARCHIVE_NUM: 0,
        INTIME_ARCHIVE_NUM: 0
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
      currentTime: new Date(), // 获取当前时间
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
    if(sessionStorage["identification"] == "Admin"){
      this.if_admin = true
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
      var year = this.currentTime.getYear() + 1900;
      var month = this.currentTime.getMonth() + 1;
      var day = this.currentTime.getDate();
      var hour = this.currentTime.toTimeString();
      var wholetime = year+'-'+month+'-'+day+' '+hour.slice(0,8)
      return wholetime
    },
    insert_data() {
      if (this.solve_result == "超期结办") {
        this.form["OVERTIME_ARCHIVE_NUM"] = 1;
        this.form["INTIME_TO_ARCHIVE_NUM"] = 0;
        this.form["INTIME_ARCHIVE_NUM"] = 0;
      } else if (this.solve_result == "处置中") {
        this.form["OVERTIME_ARCHIVE_NUM"] = 0;
        this.form["INTIME_TO_ARCHIVE_NUM"] = 1;
        this.form["INTIME_ARCHIVE_NUM"] = 0;
      } else if (this.solve_result == "按期结办") {
        this.form["OVERTIME_ARCHIVE_NUM"] = 0;
        this.form["INTIME_TO_ARCHIVE_NUM"] = 0;
        this.form["INTIME_ARCHIVE_NUM"] = 1;
      }
      debugger
      this.form["CREATE_TIME"] = this.get_time();
      debugger
      var that = this;
      var values = []
      values.push(this.form);
      axios
        .post("http://localhost:5000/insert", {
          values
        })
        .then(function(response) {
          debugger;
          if(response.data.result == '成功'){
            alert("插入成功！")
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style></style>
