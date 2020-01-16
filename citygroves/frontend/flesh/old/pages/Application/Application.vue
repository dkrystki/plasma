<template>
  <div>
        <v-btn block color="success" @click="goBack">Back</v-btn>
<!--        <md-card >-->
<!--          <md-card-content v-if="this.application !== null">-->
<!--            <v-row>-->
<!--              <v-col cols="12" md="6">-->
<!--                <Person :id="this.application.person.id"/>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="6">-->
<!--                <Address :id="this.application.current_address.id"/>-->
<!--              </v-col>-->
<!--            </v-row>-->
<!--            <v-row>-->
<!--              <v-col v-for="r of this.application.referrers" v-bind:key="r.id" cols="12" md="6">-->
<!--                <Referrer :id="r.id"/>-->
<!--              </v-col>-->
<!--            </v-row>-->
<!--            <v-row>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-field>-->
<!--                  <label>Unit Number</label>-->
<!--                  <md-input v-model="unit_number" @change="onChange"/>-->
<!--                </md-field>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-field>-->
<!--                  <label>Room Number</label>-->
<!--                  <md-input v-model="room_number" @change="onChange"/>-->
<!--                </md-field>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="3">-->
<!--                <md-field>-->
<!--                  <label>Number of people to move in</label>-->
<!--                  <md-input v-model="number_of_ppl_to_move_in" @change="onChange"/>-->
<!--                </md-field>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="3">-->
<!--                <md-datepicker v-model="move_in_date">-->
<!--                  <label>Move in date</label>-->
<!--                </md-datepicker>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-checkbox v-model="guarantor_will_pay" @change="onChange">Guarantor will pay</md-checkbox>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-checkbox v-model="centerlink_will_pay" label="Centerlink will pay" @change="onChange">Centerlink-->
<!--                  will pay-->
<!--                </md-checkbox>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-checkbox v-model="is_employed" @change="onChange">Is employed</md-checkbox>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-checkbox v-model="have_sufficient_funds" @change="onChange">Have sufficient fund</md-checkbox>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-checkbox v-model="is_local_student" @change="onChange">Is a local student</md-checkbox>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-checkbox v-model="is_international_student" @change="onChange">Is an international student-->
<!--                </md-checkbox>-->
<!--              </v-col>-->
<!--              <v-col cols="12" md="2">-->
<!--                <md-checkbox v-model="is_young_professional" @change="onChange">Is a young professinal</md-checkbox>-->
<!--              </v-col>-->
<!--            </v-row>-->
<!--          </md-card-content>-->
<!--          <md-card-actions>-->
<!--            <v-spacer/>-->
<!--              <md-button class="md-primary" @click="downloadLease">Download lease</md-button>-->
<!--            <v-spacer/>-->
<!--              <md-button class="md-primary" @click="goBack">Finalise</md-button>-->
<!--            <v-spacer/>-->
<!--          </md-card-actions>-->
<!--        </md-card>-->
  </div>
</template>

<script lang="ts">
    import {Manager} from "@/apis/manager"
    import Person from "@/components/Person.vue"
    import Address from "@/components/Address.vue"
    import Referrer from "@/components/Referrer.vue"

    let manager = new Manager();
    export default {
        data(): Object {
            return {
                loading: false,
                application: null,
                unit_number: 1,
                room_number: 1,
                current_address: "",
                number_of_ppl_to_move_in: 1,
                move_in_date: "2020-11-20",
                guarantor_will_pay: false,
                is_employed: false,
                centerlink_will_pay: false,
                have_sufficient_funds: false,
                is_local_student: false,
                is_international_student: false,
                is_young_professional: false,
            }
        },
        components: {
            Person,
            Address,
            Referrer
        },
        async created() {
            await this.refresh();
        },
        watch: {
            move_in_date: function (val) {
                this.application.move_in_date = val;
                this.application.save();
            }
        },
        methods: {
            goBack() {
                this.$router.go(-1);
            },
            downloadLease() {
                this.application.getLease();
            },
            onChange() {
                this.application.unit_number = this.unit_number;
                this.application.room_number = this.room_number;
                this.application.current_address = this.current_address;
                this.application.number_of_ppl_to_move_in = this.number_of_ppl_to_move_in;
                this.application.move_in_date = this.move_in_date;
                this.application.guarantor_will_pay = this.guarantor_will_pay;
                this.application.is_employed = this.is_employed;
                this.application.centerlink_will_pay = this.centerlink_will_pay;
                this.application.have_sufficient_funds = this.have_sufficient_funds;
                this.application.is_local_student = this.is_local_student;
                this.application.is_international_student = this.is_international_student;
                this.application.is_young_professional = this.is_young_professional;
                this.application.save();
            },
            async refresh() {
                this.loading = true;
                this.application = await manager.applications.get(Number(this.$route.params.id));

                this.unit_number = this.application.room.unit.number;
                this.room_number = this.application.room.number;
                this.current_address = this.application.current_address;
                this.number_of_ppl_to_move_in = this.application.number_of_ppl_to_move_in;
                this.move_in_date = this.application.move_in_date;
                this.guarantor_will_pay = this.application.guarantor_will_pay;
                this.is_employed = this.application.is_employed;
                this.centerlink_will_pay = this.application.centerlink_will_pay;
                this.have_sufficient_funds = this.application.have_sufficient_funds;
                this.is_local_student = this.application.is_local_student;
                this.is_international_student = this.application.is_international_student;
                this.is_young_professional = this.application.is_young_professional;
            },
        }
    };
</script>

