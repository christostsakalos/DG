<template>
    <div class="page-dashboard">
                <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
            </ul>
        </nav>

<div class="columns is-multiline">
    <div class="column">
        <p class="subtitle">Incomplete Jobs</p> <Completechart />
    </div>
    <div class="column">
     <p class="subtitle">Unpaid Jobs</p>   <Paidchart />
    </div>

</div>
    </div>
</template>

<script>
import Completechart from '@/components/charts/Completechart'
import Paidchart from '@/components/charts/Paidchart';
export default {
    name: 'Dashboard',
    components: {Completechart, Paidchart},
}
</script>