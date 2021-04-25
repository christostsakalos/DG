<template>
    <div class="page-categories">

<div style="display: flex;">
        
    <div style="flex: 0.7;height: 200px; background-color: #f4f5f8">
      Parent Categories<br>  <router-link :to="{ name: 'AddCategory' }" class="button is-success mt-4">Add category</router-link>
<Parentcategories />
    </div>
<br>
    <div class="divider is-vertical">
       
    </div>
    <div style="flex: 1;height: 200px; background-color: #f4f5f8">
     Sub Categories:<br>    <router-link :to="{ name: 'AddSubcategory' }" class="button is-success mt-4">Add subcategory</router-link>
    <Subcategories />
    </div>
    </div>
    <div class="columns">
        <br>
    </div><br><br><br><br><br><br><br><br><br><br><br><br>
    </div>


</template>




<script>
import {ref, onMounted, useRouter} from 'vue';
import { toast } from 'bulma-toast';
import axios from 'axios'
import Parentcategories from './components/Parentcategories'
import Subcategories from './components/Subcategories'
export default {
    name : 'Categories',
    components: {Parentcategories, Subcategories}
    
}
</script>

<style scoped>

</style>