<template>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
    name: 'CategoryDelete',

    mounted() {
        this.deleteSubcategory()
    },
    methods: {
        deleteSubcategory() {
            const subcategoryID = this.$route.params.id
            if (confirm('Are you sure you want to delete this category?')){
            axios
                .delete(`/api/v1/subcategories/${subcategoryID}`)
                .then(response => {
                    toast({
                        message: 'The category has been removed',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right',
                    })                 
                    this.$router.push('/categories')
                
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })}
        }
    }
}
</script>