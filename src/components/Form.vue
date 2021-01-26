<template>
  <div>
    <md-field md-clearable>
      <label>ชื่อผู้ให้ข้อมูล</label>
      <md-input v-model='pname'></md-input>
      <span class='md-helper-text'>ตัวอย่าง สมมติ เกตมณี </span>
    </md-field>
    <md-field md-clearable>
      <label>เบอร์โทร</label>
      <md-input v-model='tel'></md-input>
      <span class='md-helper-text'>ตัวอย่าง 0812345678 </span>
    </md-field>
    <md-field>
      <label>อีเมล</label>
      <md-input v-model='email'></md-input>
      <span class='md-helper-text'>ตัวอย่าง example@exmaple.com </span>
    </md-field>
    <md-field>
      <label for='ministry'>กระทรวง</label>
      <md-select v-model='selectedMinistry' name='ministry' id='ministry' @md-selected='onMinistryChange($event)' >
        <md-option v-for="item in ministry" v-bind:key="item" :value="item.key">
            {{item.name}}
        </md-option>
      </md-select>
    </md-field>
    <md-field>
      <label for='department'>กรม</label>
      <md-select
        v-model='selectedDepartment'
        name='department'
        id='department'
        :disabled='department == null'
      >
        <md-option
          v-for='item in department' v-bind:key='item' :value="item.key"
          >{{ item.name }}
        </md-option>
      </md-select>
    </md-field>
  </div>
</template>

<script>
export default {
  name: 'TextFields',
  data: () => ({
    pname: '',
    tel: '',
    email: '',
    ministry: [
      { name: 'กระทรวง1', key: '1' },
      { name: 'กระทรวง2', key: '2' }
    ],
    department: null,
    selectedMinistry: null,
    selectedDepartment: null,
    type: null,
    withLabel: null,
    inline: null,
    number: null,
    textarea: null,
    autogrow: null,
    disabled: null
  }),
  methods: {
    onMinistryChange: function onMinistryChange (event) {
      this.department = [
        { name: 'Grom A', key: 'ga' },
        { name: 'Grom B', key: 'gb' }
      ]
    }
  }
}
</script>
