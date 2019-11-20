<template>
  <div class="wrapper">
    <side-bar>
      <mobile-menu slot="content"></mobile-menu>
      <sidebar-link to="/admin/login">
        <i class="nc-icon nc-atom"></i>
        <p>登录</p>
      </sidebar-link>
      <sidebar-link to="/admin/Livelihood">
        <i class="nc-icon nc-circle-09"></i>
        <p>反馈统计</p>
      </sidebar-link>
      <sidebar-link to="/admin/eventsdeal">
        <i class="nc-icon nc-notes"></i>
        <p>事件及处理</p>
      </sidebar-link>
      <sidebar-link to="/admin/streetevent">
        <i class="nc-icon nc-paper-2"></i>
        <p>社区事件统计</p>
      </sidebar-link>
      <sidebar-link to="/admin/graph">
        <i class="nc-icon nc-bell-55"></i>
        <p>大数据分析</p>
      </sidebar-link>
    </side-bar>
    <div class="main-panel">
      <top-navbar></top-navbar>

      <dashboard-content @click="toggleSidebar">

      </dashboard-content>

      <content-footer></content-footer>
    </div>
  </div>
</template>
<style lang="scss">

</style>
<script>
  import TopNavbar from './TopNavbar.vue'
  import ContentFooter from './ContentFooter.vue'
  import DashboardContent from './Content.vue'
  import MobileMenu from './MobileMenu.vue'
  export default {
    components: {
      TopNavbar,
      ContentFooter,
      DashboardContent,
      MobileMenu
    },
    methods: {
      toggleSidebar () {
        if (this.$sidebar.showSidebar) {
          this.$sidebar.displaySidebar(false)
        }
      }
    }
  }

</script>
