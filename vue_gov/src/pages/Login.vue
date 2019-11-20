<template>
  <div class="content">
    <div class="container-fluid">
      <div class="input-area" v-if="identification == 'traveler'">
        <img
          src="../assets/img/home_trade_marker.png"
          width="50%"
          class="home_img"
          />
        <mu-icon size="60" value="people"></mu-icon>
        <div>
          <input
            type="text"
            class="qxs-ic_user qxs-icon"
            placeholder="用户名"
            v-model="userName"
            ref="login_name"
          />
        </div>
        <div>
          <input
            type="text"
            class="qxs-ic_password qxs-icon"
            placeholder="密码"
            v-model="password"
            ref="login_password"
          />
        </div>
          <li>
            <input
              type="text"
              class="qxs-ic_password qxs-icon"
              placeholder="验证码"
              v-model="checkcode"
              ref="login_checkcode"
            />
            dsds
          </li>
        <div>
          <p ref="show"></p>
          <mu-button v-on:click="login">登陆</mu-button>
        </div>
      </div>
      <div class="input-area" v-if="identification == 'login_user'">
        <mu-icon size="200" value="people"></mu-icon>
        <div>用户名：hty</div>
        <div>信息：</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "app",
  data() {
    return {
      identification: "traveler",
      user:"",
      setting:{}
    };
  },
  mounted() {
    sessionStorage.setItem("identification",this.identification)
  },
  methods: {
    login() {
      var nm = this.$refs.login_name.value;
      var pw = this.$refs.login_password.value;
      var that = this
      axios
        .post("http://localhost:5000/authentication", {
          name: nm,
          password: pw
        })
        .then(function(response) {
          console.log(response);
          if (response.data.Authentication === "Yes") {
            that.identification = "login_user"
            sessionStorage.setItem("identification",that.identification)
          } else {
            alert("Fail");
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
    generatedCode () {
      const random = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
      let code = ''
      for (let i = 0; i < 4; i++) {
        let index = Math.floor(Math.random() * 36)
        code += random[index]
      }
      this.ccode = code
    },
     checkCode () {
      let vcode = this.loginInfo.vcode
      vcode = vcode.toUpperCase()
      let ccode = this.ccode
      ccode = ccode.toUpperCase()
      if (vcode !== ccode) {
        this.$message.error('Please enter the correct verification code!')
        this.$set(this.loginInfo, 'vcode', '')
        this.$set(this.loginInfo, 'password', '')
      } else {
        return 1
      }
    }
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
