<template>
  <div class="content">
    <div class="container-fluid">
      <div class="wall-wrap">
        <div class="wall-main" style="position: relative; height:100%;">
          <div class="wall-logo">
            <div class="input-area" v-if="1">
              <img src="../assets/img/home_trade_marker.png" width="50%" class="home_img" />
              <mu-icon size="60" value="people"></mu-icon>
              <div>
                <ul>
                <li>
                  <img src="../assets/img/icons/2x/baseline_account_box_black_18dp.png" alt="">
                  <input type="text" class="login-name" placeholder="用户名" v-model="userName" ref="login_name" />
                </li>
                <li>
                  <img src="../assets/img/icons/2x/baseline_lock_black_18dp.png" alt="">
                  <input type="password" class="login-password" placeholder="密码"   v-model="password" ref="login_password" id = "pw"/>
                  <img src="../assets/img/icons/2x/baseline_visibility_black_18dp.png" v-show="if_visible == true" v-on:click="change_vis">
                  <img src="../assets/img/icons/2x/baseline_visibility_off_black_18dp.png" v-show="if_visible == false" v-on:click="change_vis">
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
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return{
      if_visible: false
    }
  },
  methods:{
    change_vis() {
      this.if_visible = !this.if_visible
      debugger
      var p = document.getElementById("pw")
      debugger
      if(this.if_visible ==true)
        p.type = "text"
      else
        p.type = "password"
    },
    is_see() {
      if (this.if_visible == true)
        return "text"
      else
        return "password"
    }
  }
}
</script>

<style>
.wall-wrap {
  line-height: 16px;
  color: #000;
  font-size: 12px;
  font-weight: normal;
  -webkit-font-smoothing: antialiased;
  padding: 0;
  font-family: 'Microsoft Yahei';
  margin: 0 auto;
  position: absolute;
  left: 50%;
  top: 50%;
  margin-top: -315px;
  margin-left: -200px;
  width: 400px;
  height: 630px;
  background: #ffffff;
  box-shadow: 0 0 10px 0 rgba(0, 33, 79, 0.11);
  border-radius: 6px;
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
  /* padding-left: 55px; */
  border-radius: 10px;
  line-height: 20px;
  margin: 10px 0;
  outline: none;
  border: 1px solid rgba(209, 204, 204, 0.897);
}
.input-area {
  padding-top: 15%;
  display: flex;
  /* flex-direction: column; */
  /* align-items: center; */
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
.login-check {
  width: 200px;

}
</style>
