<template>
  <Card v-if="application !== null" :title="application.getTitle()">
    <v-row>
      <v-col cols="12" md="6">
        <Person :id="application.person.id"/>
      </v-col>
      <v-col cols="12" md="6">
        <Address :id="application.current_address.id"/>
      </v-col>
    </v-row>
    <v-row>
      <v-col v-for="r of application.referrers" v-bind:key="r.id" cols="12" md="6">
        <Referrer :id="r.id"/>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="12" md="2">
        <v-text-field v-model="unit_number" label="Unit Number" @change="onChange"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-text-field v-model="room_number" label="Room Number" @change="onChange"/>
      </v-col>
      <v-col cols="12" md="3">
        <v-text-field v-model="number_of_ppl_to_move_in" label="Number of people to move in" @change="onChange"/>
      </v-col>
      <v-col cols="12" md="3">
        <v-text-field v-model="move_in_date" label="Move in date" @change="onChange"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox v-model="guarantor_will_pay" @change="onChange" label="Guarantor will pay"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox v-model="centerlink_will_pay" @change="onChange" label="Centerlink will pay"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox v-model="is_employed" @change="onChange" label="Is employed"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox v-model="have_sufficient_funds" @change="onChange" label="Have sufficient fund"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox v-model="is_local_student" @change="onChange" label="Is a local student"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox v-model="is_international_student" @change="onChange" label="Is an international student"/>
      </v-col>
      <v-col cols="12" md="2">
        <v-checkbox v-model="is_young_professional" @change="onChange" label="Is a young professinal"/>
      </v-col>
    </v-row>
    <template #actions>
      <v-btn color="success" @click="downloadLease">Download lease</v-btn>
      <v-btn color="success">Finalise</v-btn>
    </template>
  </Card>
</template>

<script lang="ts">
    import {api} from "@/apis/backend"
    import Person from "@/components/Person.vue"
    import Address from "@/components/Address.vue"
    import Referrer from "@/components/Referrer.vue"
    import Card from "@/components/Cards/Card.vue"

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
            Referrer,
            Card
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
                this.application = await api.applications.get(Number(this.$route.params.id));

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
