<template>
  <div class="content">
    <div class="container-fluid">
      <div class="main_page">
        <div class="wall-wrap" v-if="identification == 'traveler'">
          <div class="wall-main" style="position: relative; height:100%;">
            <div class="wall-logo">
              <div class="input-area">
                <img
                  src="../assets/img/home_trade_marker.png"
                  width="50%"
                  class="home_img"
                />
                <mu-icon size="60" value="people"></mu-icon>
                <div>
                  <ul>
                    <li style="list-style:none; padding-left:20px">
                      <img
                        src="../assets/img/icons/2x/baseline_account_box_black_18dp.png"
                        alt=""
                      />
                      <input
                        type="text"
                        class="login-name"
                        placeholder="用户名"
                        v-model="userName"
                        ref="login_name"
                      />
                    </li>
                    <li style="list-style:none ; padding-left:20px">
                      <img
                        src="../assets/img/icons/2x/baseline_lock_black_18dp.png"
                        alt=""
                      />
                      <input
                        type="password"
                        class="login-password"
                        placeholder="密码"
                        v-model="password"
                        ref="login_password"
                        id="pw"
                      />
                      <img
                        src="../assets/img/icons/2x/baseline_visibility_black_18dp.png"
                        v-show="if_visible == true"
                        v-on:click="change_vis"
                      />
                      <img
                        src="../assets/img/icons/2x/baseline_visibility_off_black_18dp.png"
                        v-show="if_visible == false"
                        v-on:click="change_vis"
                      />
                    </li>
                    <li style="list-style:none">
                      <iframe
                        src="http://localhost:8001/slider.html"
                        frameborder="0"
                        style="width:300px;height:80px"
                      ></iframe>
                    </li>
                  </ul>
                </div>
                <div>
                  <p ref="show"></p>
                  <mu-button v-on:click="login">登陆</mu-button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-if="identification == 'login_user'">
          <error-event></error-event>
          <li style="list-style: none">
            <mu-icon
              left
              size="30"
              value="reply_all"
              v-on:click="logout"
            ></mu-icon>
            登出
          </li>
          <div class="wall-main" style="padding-top:50px;">
            <mu-container>
              <mu-card style="width: 100%; max-width: 375px; margin: 0 auto;">
                <mu-card-header title="Myron Avatar" sub-title="sub title">
                  <mu-avatar slot="avatar">
                    <img src="../assets/img/logo.png" />
                  </mu-avatar>
                </mu-card-header>
                <mu-card-media title="Image Title" sub-title="Image Sub Title">
                  <img src="../assets/img/sun.jpg" />
                </mu-card-media>
                <mu-card-title
                  title="Content Title"
                  sub-title="Content Title"
                ></mu-card-title>
                <mu-card-text>
                  作为用户，你可以进行数据查询，大数据分析，异常报警查看，快去看看吧。
                </mu-card-text>
                <mu-card-actions>
                </mu-card-actions>
              </mu-card>
            </mu-container>
          </div>
        </div>
        <div v-if="identification == 'Admin'">
          <error-event></error-event>
          <li style="list-style: none">
            <mu-icon
              left
              size="30"
              value="reply_all"
              v-on:click="logout"
            ></mu-icon>
            登出
          </li>
          <div class="wall-main" style="padding-top:50px;">
            <mu-container>
              <mu-card style="width: 100%; max-width: 375px; margin: 0 auto;">
                <mu-card-header title="Myron Avatar" sub-title="sub title">
                  <mu-avatar slot="avatar">
                    <img src="../assets/img/logo.png" />
                  </mu-avatar>
                </mu-card-header>
                <mu-card-media title="Image Title" sub-title="Image Sub Title">
                  <img src="../assets/img/sun.jpg" />
                </mu-card-media>
                <mu-card-title
                  title="Content Title"
                  sub-title="Content Title"
                ></mu-card-title>
                <mu-card-text>
                  你可以作为管理员额外进行以下操作管理员
                </mu-card-text>
                <mu-card-actions>
                  <mu-button to="/admin/usermanage">用户管理</mu-button>
                  <mu-button to="/admin/updatedatabase">数据库管理</mu-button>
                </mu-card-actions>
              </mu-card>
            </mu-container>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ErrorEvent from "../pages/event.vue";
export default {
  name: "app",
  components: {
    ErrorEvent
  },
  data() {
    return {
      identification: "traveler",
      user: "",
      setting: {},
      if_visible: false,
      if_check: false
    };
  },
  mounted() {
    if (sessionStorage["identification"] != null) {
      this.identification = sessionStorage["identification"];
    }
    sessionStorage.setItem("if_check", false);
    sessionStorage.getItem;
    window.addEventListener("message", function(e) {
      if (e.data.msg == "success_check") {
        debugger;
        if (sessionStorage["if_check"] != "true") {
          sessionStorage.setItem("if_check", true);
        } else return;
      }
      console.log(e.data);
    });
  },
  methods: {
    login() {
      var nm = this.$refs.login_name.value;
      var pw = this.$refs.login_password.value;
      var that = this;
      this.if_check = sessionStorage["if_check"]
      debugger;
      if (this.if_check != "true") {
        alert("请先拖动验证");
        return;
      }

      axios
        .post("http://localhost:5000/authentication", {
          name: nm,
          password: pw
        })
        .then(function(response) {
          console.log(response);
          debugger;
          if (response.data.Authentication === "User") {
            that.identification = "login_user";
            that.login_change(that.identification, response.data);
            sessionStorage.setItem("identification", that.identification);
            alert("你现在可以作为一个注册用户行动了");
          } else if (response.data.Authentication === "Admin") {
            that.identification = "Admin";
            that.login_change(that.identification, response.data);
            sessionStorage.setItem("identification", that.identification);
            alert("你现在可以作为一个管理员行动了");
          } else {
            alert("用户名密码错误");
          }
        })
        .catch(function(error) {
          console.log(error);
        });

      // axios.get('http://127.0.0.1:5000/getMsg').then(function (response) {
      //   // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
      //   // 可以直接通过 response.data 取key-value
      //   // 坑一：这里不能直接使用 this 指针，不然找不到对象
      //   var msg = response.data.msg
      //   // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串
      //   alert('Success ' + response.status + ', ' + response.data + ', ' + msg)
      // }).catch(function (error) {
      //   alert('Error ' + error)
      // })
    },
    change_vis() {
      this.if_visible = !this.if_visible;
      debugger;
      var p = document.getElementById("pw");
      debugger;
      if (this.if_visible == true) p.type = "text";
      else p.type = "password";
    },
    is_see() {
      if (this.if_visible == true) return "text";
      else return "password";
    },
    logout() {
      this.identification = "traveler";
      sessionStorage.setItem("if_check",false);
      sessionStorage.setItem("identification", this.identification);
    },
    login_change(identification, data) {}
  }
};
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
.input-area {
  padding-top: 15%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.input-area button {
  width: 200px;
  height: 40px;
  line-height: 20px;
  background-color: #03020e;
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
.main_page {
  height: 800px;
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
