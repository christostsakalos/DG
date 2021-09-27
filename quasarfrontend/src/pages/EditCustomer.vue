<template>
    <q-btn icon="edit" btn dense color="black" class="text-white"  @click="load " />
    <q-dialog v-model="persistent" persistent transition-show="scale" transition-hide="scale">
      <q-card v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'50%'}">
        <q-card-section>
            <div class="text-center q-py-md">
              <div class="col text-h6 ellipsis">
                Edit {{initialValues.get_full_name}}

              </div>
            </div>
        </q-card-section>

        <q-card-section>
      <Form  @submit="onSubmit" :initial-values="initialValues"   :validation-schema="schema" class="q-gutter-sm">
        <div class=" row  justify-center">
         <div class="col-lg-5 col-xl-5 col-md-12 
         col-sm-12 col-xs-12 self-end  q-mr-sm">
        <Field name="email" v-slot="{ errorMessage, value, field }">
          <q-input
            label="Email"
            placeholder="user@example.com"
            color="orange-7"
            :model-value="value"
            v-bind="field"
            :error-message="errorMessage"
            :error="!!errorMessage"
          />
        </Field>

        <Field name="first_name" v-slot="{ errorMessage, value, field }">
          <q-input
            label="First Name"
            placeholder="First Name"
            color="orange-7"
            :model-value="value"
            v-bind="field"
            :error-message="errorMessage"
            :error="!!errorMessage"
          />
        </Field>
        
        <Field name="last_name" v-slot="{ errorMessage, value, field }">
          <q-input
            label="Last Name"
            placeholder="Last Name"
            color="orange-7"
            :model-value="value"
            v-bind="field"
            :error-message="errorMessage"
            :error="!!errorMessage"
          />
        </Field>
        <Field name="address" v-slot="{ errorMessage, value, field }">
          <q-input
            label="Address"
            placeholder="Address"
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
          <q-btn label="Save" type="submit"  color="black"/>
          <q-btn flat label="Close" v-close-popup />
         
        </div>
      </Form>
         </q-card-section>
      </q-card>
    </q-dialog>
</template>

<script>
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
    name: 'EditCustomer',
    emits: ['page-refresh'],
  props: {
    id: Number
  },
  setup(props, {emit}) {
    const schema = yup.object({
      email: yup.string().required().email().label("Email address"),
      first_name: yup.string().required().min(3).label("First Name"),
      last_name: yup.string().required().min(4).label("Last Name"),
      address: yup.string().required().min(4).label("Address"),
    });
    // Providing initial values for the `is_active` and `subscribed` fields
    // because q-checkbox has 3 states, in which undefined means undetermined
    // providing an explict false initial value avoids this
        const persistent = ref(false)
        const first_name = ref('');
        const last_name = ref('');
        const email = ref('');
        const address = ref('');
    const initialValues = ref({
    });
    const load = async () => {
      const response = await api.get(`customers/${props.id}`);
      initialValues.value = response.data
      persistent.value = true
    };
 const onSubmit = async (values) => {
   await api.patch(`customers/${props.id}/`,values).then( response =>{
     
     persistent.value = false
          Notify.create({
            type: 'positive',
            color: 'positive',
            timeout: 1000,
            position: 'center',
            message: `Changes Applied`,
          })
          emit('page-refresh')
          console.log(values.id)
      }).catch(error => {if (error.response) {
      for (const property in error.response.data) {
        console.log(error.response.data[property])
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
    first_name,
    last_name,
    email,
    address,
    onSubmit,
    load,
    Notify,
  
    };
  },
})
</script>