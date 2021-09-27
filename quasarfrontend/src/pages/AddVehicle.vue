<template>
  <div class="q-pr-xl q-gutter-sm">
    <q-btn label="Add Vehicle" class="text-black" color="white" @click="persistent = true" />

    <q-dialog v-model="persistent" persistent transition-show="scale" transition-hide="scale">

      <q-card v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'50%'}">
        <q-card-section>
            <div class="text-center q-py-md">
              <div class="col text-h6 ellipsis">
                Add Vehicle
              </div>
            </div>
        </q-card-section>

        <q-card-section>
      <Form  @submit="onSubmit" :initial-values="initialValues"  :validation-schema="schema" class="q-gutter-sm">
        <div class=" row  justify-center">
         <div class="col-lg-5 col-xl-5 col-md-12 
         col-sm-12 col-xs-12 self-end  q-mr-sm">
        <Field name="make" v-slot="{ errorMessage, value, field }">
          <q-input
            label="make"
            placeholder="Car Make"
            color="orange-7"
            :model-value="value"
            v-bind="field"
            :error-message="errorMessage"
            :error="!!errorMessage"
          />
        </Field>

        <Field name="model" v-slot="{ errorMessage, value, field }">
          <q-input
            label="Car Model"
            placeholder="Model"
            color="orange-7"
            :model-value="value"
            v-bind="field"
            :error-message="errorMessage"
            :error="!!errorMessage"
          />
        </Field>
        
        <Field name="vehicleregistrationnumber" v-slot="{ errorMessage, value, field }">
          <q-input
            label="Plate number"
            placeholder="Plate number"
            color="orange-7"
            :model-value="value"
            v-bind="field"
            :error-message="errorMessage"
            :error="!!errorMessage"
          />
        </Field>
        <Field name="fueltype" v-slot="{ errorMessage, value, field }">
          <q-input
            label="Fuel Type"
            placeholder="fueltype"
            color="orange-7"
            :model-value="value"
            v-bind="field"
            :error-message="errorMessage"
            :error="!!errorMessage"
          />
        </Field>
        </div>

        </div>

        <div align="right">
          <q-btn label="Add" type="submit"  color="black"  />
          <q-btn flat label="Close" v-close-popup />
         
        </div>
      </Form>
         </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script lang="ts">
import {api} from '../boot/axios'
import { Form, Field} from "vee-validate";
import { Notify } from 'quasar'
import * as yup from "yup";
import { defineComponent, ref } from 'vue'
export default defineComponent({
    components: {
    Field,
    Form,
  
  },
    name: 'AddVehicle',
  setup() {
    const schema = yup.object({
      make: yup.string().required().min(3).label("Make"),
      model: yup.string().required().min(3).label("model"),
      vehicleregistrationnumber: yup.string().required().min(3).label("Vehicle Registration Number"),
      fueltype: yup.string().required().min(4).label("Fueltype"),
        
    });
    // Providing initial values for the `is_active` and `subscribed` fields
    // because q-checkbox has 3 states, in which undefined means undetermined
    // providing an explict false initial value avoids this
        const persistent = ref(false)
        const make = ref('');
        const model = ref('');
        const vehicleregistrationnumber = ref('');
        const fueltype = ref('');
    const initialValues = {
      is_active: false,
    };
/*  function onSubmit () {
  console.log('submitted')
} */
const onSubmit = (values) => {
api.post('vehicles/',values).then(response =>{
        persistent.value = false
          Notify.create({
            type: 'positive',
            color: 'positive',
            timeout: 1000,
            position: 'center',
            message: `Customer Created`,
          })
      }).catch(error => {if (error.response) {
      for (const property in error.response.data) {
                  Notify.create({
          message: `${error.response.data[property]}`,
          type: 'negative',
          timeout: 1000,
          position: 'center',
        })
        }
        } else if (error.message) {
                              Notify.create({
          message: `${error.message}`,
          type: 'negative',
          timeout: 1000,
          position: 'center',
        })
              }
})
}
    return {
      schema,
       initialValues,
  persistent,
    make,
    model,
    vehicleregistrationnumber,
    fueltype,
    onSubmit,
    Notify,
 
  
    };
  },
})
</script>

<style lang="scss" scoped>
</style>