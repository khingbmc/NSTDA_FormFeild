<template>
  <!-- ตรวจสอบนโยบายที่เกี่ยวข้องและดาวน์โหลด Template กรอกข้อมูลจาก link หรือ QR Code -->
  <div>
    <md-steppers md-alternative>
      <md-step
        id="first"
        md-label="ขั้นตอนที่ 1:"
        md-description="ตรวจสอบนโยบายที่เกี่ยวข้องและดาวน์โหลด
      Template กรอกข้อมูลจาก link หรือ QR Code"
      >
        <div
          pbi-resize="powerbi"
          pbi-resize-src="https://app.powerbi.com/view?r=eyJrIjoiZDEzODk5ZjQtMTVhOS00NDk3LWExYTUtZWQ0OWE0OTVjZmQwIiwidCI6IjRhNGY3YjUyLTBlMDUtNDQxNS04NDU0LTc2ODliMDBhODdiMiIsImMiOjEwfQ%3D%3D"
          pbi-resize-min-width="800"
          pbi-default-width="600px"
          pbi-default-height="488"
          pbi-resize-width="16"
          pbi-resize-height="9"
          pbi-resize-load-event="page-load"
          pbi-resize-header="true"
          style="position: relative;"
        >
          <iframe frameborder="0" allowfullscreen="true"></iframe>
        </div>
      </md-step>
      <md-step
        id="second"
        md-label="ขั้นตอนที่ 2:"
        md-description="กรอกข้อมูลเบื้องต้นและอัปโหลด Template"
      >
        <div style="margin:2.5 em;">
          <md-dialog-alert
            :md-active.sync="alert_dialog"
            md-content="Success!"
            md-confirm-text="Ok!"
          />
          <md-field md-clearable>
            <label>ชื่อผู้ให้ข้อมูล</label>
            <md-input v-model="pname"></md-input>
            <span class="md-helper-text">ตัวอย่าง สมมติ เกตมณี </span>
          </md-field>
          <md-field md-clearable>
            <label>เบอร์โทร</label>
            <md-input v-model="tel"></md-input>
            <span class="md-helper-text">ตัวอย่าง 0812345678 </span>
          </md-field>
          <md-field>
            <label>อีเมล</label>
            <md-input v-model="email"></md-input>
            <span class="md-helper-text">ตัวอย่าง example@exmaple.com </span>
          </md-field>
          <md-field>
            <label for="ministry">กระทรวง</label>
            <md-select
              v-model="selectedMinistry"
              name="ministry"
              id="ministry"
              @md-selected="onMinistryChange($event)"
            >
              <md-option
                v-for="item in ministry"
                v-bind:key="item"
                :value="item.key"
              >
                {{ item.name }}
              </md-option>
            </md-select>
          </md-field>
          <md-field>
            <label for="department">กรม</label>
            <md-select
              v-model="selectedDepartment"
              name="department"
              id="department"
              :disabled="department == null"
            >
              <md-option
                v-for="item in department"
                v-bind:key="item"
                :value="item.key"
                >{{ item.name }}
              </md-option>
            </md-select>
          </md-field>
          <!-- <div class="md-layout" :class="md-alignment-center-left">
      <div class="md-layout-item md-size-25">
        <span class="md-prefix">มีระบบ data catalog</span>
      </div>
      <div class="md-layout-item md-size-25">
        <md-radio v-model="radio" :value="true">Object A</md-radio>
        <md-radio v-model="radio" :value="false">Object B</md-radio>
      </div>
    </div> -->
          <div>
            <span
              class="md-prefix"
              style="float: left; margin: 16px 16px 16px 0px;"
              >มีระบบ data catalog</span
            >
            <md-radio v-model="radio" :value="true" style="float: left;"
              >มี</md-radio
            >
            <md-radio v-model="radio" :value="false" style="float: left;"
              >ไม่มี</md-radio
            >
          </div>
          <md-field>
            <label>Upload Template</label>
            <md-file
              v-model="file.name"
              @md-change="onFileUpload($event)"
            ></md-file>
          </md-field>
          <div style="float:right;">
            <md-button
              class="md-raised md-primary"
              style="margin-bottom:2em;"
              @click="onSubmitForm($event)"
              >Submit</md-button
            >
          </div>
        </div>
      </md-step>
    </md-steppers>
    <div>
        <md-content id="faq">
          <h1>FAQ</h1>

          <p class="question">Q: ต้องเริ่มจากตรงไหน ?</p>
          <p class="answer">A: เริ่มจากหน่วยงานของตนเองก่อนจ้า</p>

          <p class="question">Q: ต้องเริ่มจากตรงไหน ?</p>
          <p class="answer">A: เริ่มจากหน่วยงานของตนเองก่อนจ้า</p>

        </md-content>
      </div>
    <div id="container">
      <div id="contacts">
        <table id="table">
          <tr>
            <p style="text-align:right;">สอบถามข้อมูลเพิ่มเติมโทร</p>
          </tr>
          <tr>
            <p style="text-align:right;">โทร: 080-0000000</p>
          </tr>
          <tr>
            <p style="text-align:right;">Email test@gmail.com</p>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>
<style>
@import url("https://fonts.googleapis.com/css?family=Open+Sans");

#container {
  padding-top: 20px;

  width: 100vw;
  color: white;
  background-color: #292354;

  height: 12em;
}
#contacts {
  width: 100%;
}
#faq {
    width: 100%;
    padding-left: 2em;
    padding-top: 2em;
    text-align: start;
    height: 15em;
    color: black;
    margin: 0%;
    background-color: rgb(160, 185, 231);
    justify-content:flex-start;
    align-items:center;
  }
.question{
  font-weight: bold;
  color: rgb(82, 116, 228);
  margin-bottom: 0%;
}
.answer{
margin-top: 0%;
font-weight: bold;
}
#table {
  align-content: flex-end;
  width: 100%;
  padding-right: 2%;
}
</style>
<script>
export default {
  name: "TextFields",
  data: () => ({
    pname: "",
    tel: "",
    email: "",
    // ministry: [
    //   { name: 'กระทรวง1', key: '1' },
    //   { name: 'กระทรวง2', key: '2' }
    // ],
    ministry: null,
    department: null,
    selectedMinistry: null,
    selectedDepartment: null,
    radio: false,
    file: { name: "" },
    type: null,
    withLabel: null,
    inline: null,
    number: null,
    textarea: null,
    autogrow: null,
    disabled: null,
    alert_dialog: false
  }),
  methods: {
    onFileUpload(evt) {
      this.file = evt[0];
    },
    onMinistryChange: function onMinistryChange(event) {
      this.department = null;
      this.selectedDepartment = null;
      this.axios
        .get("http://35.197.128.3:8000/dep?ministry=" + this.selectedMinistry)
        .then(response => {
          this.department = response.data;
          console.log(response.data);
        });
    },

    onSubmitForm: function onSubmitForm(event) {
      const formData = new FormData();

      formData.append("name", this.pname);
      formData.append("phone_number", this.tel);
      formData.append("email", this.email);
      formData.append("ministry", this.selectedMinistry);
      formData.append("department", this.selectedDepartment);
      formData.append("template_upload", this.file);

      console.log(formData);
      this.alert_dialog = true;
      this.axios
        .post("http://35.197.128.3:8000/submit", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(function() {
          console.log("SUCCESS!!");
        })
        .catch(function(err) {
          console.log("FAILURE!!");
          console.log(err);
        });
    }

    //   onSubmitForm: function onSubmitForm(event) {
    //     this.axios.post("http://127.0.0.1:8000/submit",
    //     { name: this.pname, phone_number: this.tel, ministry: this.selectedMinistry, department : this.selectedDepartment, email : this.email }).then(response => {
    //     console.log("response: ", response)
    //   // do something about responsethi
    // }).catch(err => {
    //   console.error(err)
    // });

    //    }
  },
  mounted: function() {
    this.axios.get("http://35.197.128.3:8000/min").then(response => {
      this.ministry = response.data;
      console.log(response.data);
    });
  }
};
</script>
