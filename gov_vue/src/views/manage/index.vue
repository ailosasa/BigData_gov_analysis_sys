<template>
  <div class="manage tc">
    <button v-on:click="add">新增</button>
    <div class="input-area" v-show="showAdd">
        <input type="text" placeholder="请输入人员姓名" v-model="nameValue">
        <button v-on:click="addName">确定</button>
    </div>
    <table>
        <tr>
            <th>姓名</th>
            <th>操作</th>
        </tr>
        <tr v-for="(item,index) in peoples">
            <td>{{item.name}}</td>
            <td v-bind:id="index"><span v-on:click="edit">编辑</span><span v-on:click="del">删除</span></td>
        </tr>
    </table>
    <div class = "wrap" v-show="showEdit">
      <div class="content">
        <input type="text" placeholder="请输入姓名" v-model="newName">
        <button v-on:click="cancel">取消</button>
        <button v-on:click="editName">确定</button>
      </div>
    </div>
    <footer-nav v-bind:class="{'isManage':isNowPage}"></footer-nav>
    <!-- <footer-nav></footer-nav> -->
  </div>
</template>

<style>

</style>

<script>
import FooterNav from '../../components/footer.vue'
  export default {
    components:{
      FooterNav
    },
    data(){
        return{
            isNowPage: true,
            showAdd: false,
            showEdit: false,
            peoples: [{'name':'jack'},{'name':'joe'}],
            nameValue: '',
            newName: '',
            editId:0
        }
    },
    methods:{
      add(){
        this.showAdd = true
      },
      addName(){
        var v = this.nameValue
        if(v.trim() == ""){
          alert("请输入新增人员姓名")
        }else{
          var data = {}
          data.name = v
          this.peoples.push(data)
        }
      },
      del(e){
        var id = e.target.offsetParent.id
        this.peoples.splice(id,1)
      },
      edit(e){
        var id = e.target.offsetParent.id
        this.showEdit = true
        this.editId = id
        this.newName = this.parents[id].name
      },
      cancel(){
        this.showEdit = false
      },
      editName(){
        var v = this.newName
        if(v.trim() == ""){
          alert("请输入姓名")
        }else{
          this.peoples[this.editId].name = v
          this.showEdit = false
        }
      }
    }
  }
</script>>
