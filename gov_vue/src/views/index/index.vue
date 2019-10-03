
<template>

 <mu-paper :z-depth="1" class="demo-list-wrap">
  <mu-appbar color="teal">
    <mu-button icon slot="left">
      <mu-icon value="menu"></mu-icon>
    </mu-button>
    Menus
  </mu-appbar>
  <mu-list>
    <mu-list-item button :ripple="false">
      <mu-list-item-action>
        <mu-icon value="inbox"></mu-icon>
      </mu-list-item-action>
      <mu-list-item-title>Inbox</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button :ripple="false">
      <mu-list-item-action>
        <mu-icon value="grade"></mu-icon>
      </mu-list-item-action>
      <mu-list-item-title>Stared</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button :ripple="false">
      <mu-list-item-action>
        <mu-icon value="send"></mu-icon>
      </mu-list-item-action>
      <mu-list-item-title>Sent mail</mu-list-item-title>
    </mu-list-item>
    <mu-list-item button :ripple="false">
      <mu-list-item-action>
        <mu-icon value="drafts"></mu-icon>
      </mu-list-item-action>
      <mu-list-item-title>Drafts</mu-list-item-title>
    </mu-list-item>
  </mu-list>
  <mu-divider></mu-divider>
  <mu-list>
    <mu-list-item button :ripple="false">
      <mu-list-item-title>All mail</mu-list-item-title>
      <mu-list-item-action>
        <mu-icon value="info"></mu-icon>
      </mu-list-item-action>
    </mu-list-item>
    <mu-list-item button :ripple="false">
      <mu-list-item-title>Trash</mu-list-item-title>
      <mu-list-item-action>
        <mu-icon value="info"></mu-icon>
      </mu-list-item-action>
    </mu-list-item>
    <mu-list-item button :ripple="false">
      <mu-list-item-title>Spam</mu-list-item-title>
      <mu-list-item-action>
        <mu-icon value="info"></mu-icon>
      </mu-list-item-action>
    </mu-list-item>
    <mu-list-item button :ripple="false">
      <mu-list-item-title>Follow up</mu-list-item-title>
      <mu-list-item-action>
        <mu-icon value="info"></mu-icon>
      </mu-list-item-action>
    </mu-list-item>
  </mu-list>
</mu-paper>

</template>



<style>
.manage {
  padding-bottom: 50px;
}
.manage > button {
  width: 200px;
  height: 40px;
  line-height: 40px;
  background-color: #41b883;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
}
table {
  width: 100%;
  max-width: 500px;
  margin: 0 auto;
  margin-top: 20px;
}
.input-area input {
  width: 200px;
  height: 40px;
  line-height: 40px;
  margin: 20px 0;
  outline: none;
  border: 1px solid #333;
}
.input-area button {
  width: 60px;
  height: 40px;
  line-height: 40px;
  background-color: #41b883;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
}
th,
td {
  width: 100px;
}
tr input {
  width: 100px;
  height: 30px;
  padding-left: 10px;
  outline: none;
  border: 1px solid #333;
}
.wrap {
  display: table;
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.8);
  z-index: 10;
}
.wrap .content {
  display: table-cell;
  vertical-align: middle;
}
.wrap .content input {
  height: 40px;
  line-height: 40px;
  display: block;
  margin: 0 auto;
  margin-bottom: 10px;
  font-size: 16px;
}
.wrap .content button {
  width: 100px;
  height: 30px;
  line-height: 30px;
  background-color: #41b883;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  color: #fff;
}
</style>

<style>
.icon-container {
  display: flex;
  width: 300px;
  justify-content: space-around;
}
.icon-container .mu-icon {
  margin-bottom: 12px;
}
</style>

<script>
import FooterNav from "../../components/footer.vue";
export default {
  components: {
    FooterNav
  },
  data() {
    return {
      isNowPage: true
    };
  }
};
</script>
