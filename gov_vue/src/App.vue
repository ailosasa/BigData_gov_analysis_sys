<template>
  <section height=1000px>
    <div class="home_siderbar">
      <mu-list height=100%>
        <mu-list-item>
          <mu-button
            icon
            color="primary"
          >
            <mu-icon value="grade"></mu-icon>
          </mu-button>
        </mu-list-item>
        <mu-list-item>
          <mu-button
            :secondary="true"
            :fullWidth="true"
          >登陆
          </mu-button>
        </mu-list-item>
        <mu-list-item>
          <mu-button
            :secondary="true"
            :fullWidth="true"
          >未命名
          </mu-button>
        </mu-list-item>
        <mu-list-item>
          <mu-button
            :secondary="true"
            :fullWidth="true"
          >未命名
          </mu-button>
        </mu-list-item>
      </mu-list>
    </div>

    <div class="homepage">
      <mu-list>
        <!-- <mu-list-item>
          <mu-appbar class="home_topbar">
            <mu-button
              icon
              slot="left"
            >
              <mu-icon value="menu"></mu-icon>
            </mu-button>
            Title
            <mu-menu slot="right">
              <mu-button flat>MENU</mu-button>
              <mu-list slot="content">
                <mu-list-item button>
                  <mu-list-item-content>
                    <mu-list-item-title>Menu Item 1</mu-list-item-title>
                  </mu-list-item-content>
                </mu-list-item>
                <mu-list-item button>
                  <mu-list-item-content>
                    <mu-list-item-title>Menu Item 2</mu-list-item-title>
                  </mu-list-item-content>
                </mu-list-item>
              </mu-list>
            </mu-menu>
          </mu-appbar>
        </mu-list-item> -->

        <div class="login_page">
          <img
            src="./assets/home_trade_marker.png"
            width="100%"
            class="home_img"
          >
          <div class="input-area">
            <mu-icon
              size="60"
              value="people"
            ></mu-icon>
            <div><input
                type="text"
                class="qxs-ic_user qxs-icon"
                placeholder="用户名"
                v-model="userName"
              >
            </div>
            <div>
              <input
                type="text"
                class="qxs-ic_password qxs-icon"
                placeholder="密码"
                v-model="password"
              ></div>
            <!-- </div> -->
            <!--<button class="login_btn el-button el-button&#45;&#45;primary is-round" type="primary" round>登录</button>-->
            <button v-on:click="login">登陆</button>
          </div>
        </div>

      </mu-list>
      <mu-bottom-nav class="down_leader">
        <mu-bottom-nav-item
          title="treaty"
        >协议</mu-bottom-nav-item>
        <mu-bottom-nav-item
          title="privaty"
        >隐私</mu-bottom-nav-item>
        <mu-bottom-nav-item
          title="help"
        >帮助</mu-bottom-nav-item>
      </mu-bottom-nav>
    </div>
  </section>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      docked: false,
      open: true,
      position: "left"
    };
  }
};
</script>

<style>
@import "https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css";
@import "https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic";

.home_siderbar {
  background-color: #3622e6;
  float: left;
  width: 30%;
  /* height: calc(100vh - 300px); */
  height: 1000px;
  position: fixed;
}
.homepage {
  float: right;
  width: 70%;
  height: 1000px;
  
}
.home_topbar {
  background-color: #3622e6;
  width: 100%;
  color: yellow;
  
}
.login_page {
  padding-top: 20%;
  padding-left: 10%;
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
.qxs-ic_user {
  background-size: 20px 20px;
  background-position: 3%;
}
.qxs-ic_password {
  background-size: 20px 20px;
  background-position: 3%;
  margin-bottom: 20px;
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
  line-height: 40px;
  background-color: #3622e6;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
}
.down_leader {
  position: fixed;
  bottom: 0;
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
