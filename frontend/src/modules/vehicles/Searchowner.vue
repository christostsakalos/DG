<template>
<div class="columns">
    <div class="column">
<div class="control">
    <input class="input is-primary" type="text" autocomplete="off" placeholder="Search Owner" @keyup="getOwner" v-model="owner" @input="filteredOwners.value"  @focus="modal = true">
  <div v-if="modal">
    <ul>
      <li v-for="owner in owners" @click="setOwner(owner)" v-bind:key="owner.id"> {{ owner.first_name}} {{owner.last_name}}</li>
    </ul>
  </div>
  </div>
    </div>
</div>
</template>

<script>
///Not in use /// Will update to it later
import {ref, onMounted} from 'vue'
import axios from 'axios'
export default {
    name: 'Searchowner',
     setup() {
         var owner = ref('')
        var owners = ref([]);
        var modal = ref(false);
        const filteredOwners = ref([]);


    const setOwner = async (owner) =>{
      owner.value = owner
      modal.value = false;
      console.log(owner)
    }

    const filterOwners = async () =>{
        if (owner.value.length !== 0){
            filteredOwners.value = owner.value
            console.log(filterOwners.value)
            
        }
    }

      const getOwner = async () => {
      const response = await axios.get(`api/v1/customers/?search=${owner.value}`);
      owners.value = response.data.data;
        }


      return{
          getOwner,
          owners,
          owner,
          modal,
          setOwner,
          filterOwners,
          filteredOwners

      }
    }, 

}

  function newFunction(owner) {
    return owner.value
  }
</script>