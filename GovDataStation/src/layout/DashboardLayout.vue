<template>
  <div class="wrapper">
    <side-bar>
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/admin/login">
        <i class="nc-icon nc-atom"></i>
        <p>登录</p>
      </sidebar-link>
      <sidebar-link to="/admin/graph">
        <i class="nc-icon nc-bell-55"></i>
        <p>大数据分析</p>
      </sidebar-link>
      <sidebar-link to="/admin/updatedatabase">
        <i class="nc-icon nc-bell-55"></i>
        <p>数据添加</p>
      </sidebar-link>
      <sidebar-link to="/admin/searchdata">
        <i class="nc-icon nc-bell-55"></i>
        <p>数据查询</p>
      </sidebar-link>
      <sidebar-link to="/admin/unsolvedrole">
        <i class="nc-icon nc-bell-55"></i>
        <p>未办结事件展示</p>
      </sidebar-link>
    </side-bar>
    <div class="main-panel">
      <!-- <error-event></error-event> -->
      <dashboard-content @click="toggleSidebar"> </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./TopNavbar.vue";
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu.vue";
export default {
  components: {
    TopNavbar,
    ContentFooter,
    DashboardContent,
    MobileMenu,
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    }
  }
};
</script>
