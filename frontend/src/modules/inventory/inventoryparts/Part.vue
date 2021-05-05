<template>
    <div class="page-part">
        <Languages />
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">{{ $t("Dashboard") }}</router-link></li>
                <li><router-link to="/parts">{{ $t("Parts") }}</router-link></li>
                <li><router-link :to="{ name: 'Part', params: { id: part.id }}">{{ part.name }}</router-link></li>
            </ul>
        </nav>
        <div class="columns is-centered">
            <div class="column is-4">
                <h1 class="title">{{ part.name }}</h1>

                 <router-link :to="{ name: 'PartEdit', params: { id: part.id }}" class="button is-light mt-4">{{ $t("Edit") }}</router-link>
                 <br>
                 <router-link :to="{ name: 'PartDelete', params: { id: part.id }}" class="button is-danger mt-4">{{ $t("Delete") }}</router-link>
            </div>

            <div class="column is-4">
                <h2 class="subtitle">{{ $t("Category") }}</h2>

                <div class="table-container"> <h2 class="subtitle"><strong>{{part.category_name}}</strong></h2>
                <p>{{ $t("Name") }}: <strong>{{part.name}}</strong></p>
                <p>{{ $t("Description") }}: {{part.description}}</p>
                <p>{{ $t("Quantity") }}: {{part.quantity}}</p>
            </div>
            </div>

        </div>
      


    </div>
</template>

<script>
import axios from 'axios'
import Languages from '@/components/Languages.vue';
export default {
    name: 'Part',
    components: {Languages},
    data () {
        return {
            part: {},
        }
    },
    mounted() {
        this.getPart()
    },
    methods: {
        getPart() {
            const partID = this.$route.params.id

            axios
                .get(`/api/v1/parts/${partID}`)
                .then(response => {

                    this.part = response.data
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>