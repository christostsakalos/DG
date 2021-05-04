<template>
    <div class="page-add-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Category</h1>
            </div>
            <div class="column is-6">
                <div class="field">
                    <label>Name</label>
                    
                    <div class="control">
                        <input type="text" name="name" class="input" v-model="name">
                    </div>
                </div>


            </div>
            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click.prevent="SubmitForm">Submit</button>
                    </div>
              
                </div>
              
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import {ref, onMounted} from 'vue';
import {useRouter} from 'vue-router';
import { toast } from 'bulma-toast'

export default {
    name: 'AddCategory',
    
    setup(){
        const router = useRouter();
        const name = ref('');
       


        const SubmitForm = async() =>{
            await axios.post('/api/v1/categories/',
            {
                name: name.value
                
            }); 
            //Toast:      
            toast({
                    message: 'The category was added',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                    })
             // Toast end //
            await router.push('/categories')
        }
        return{
            SubmitForm,
            name
        }
    },
}
</script>

<style scoped>

</style>