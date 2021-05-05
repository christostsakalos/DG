<template>
    <div class="page-dashboard">
                <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
            </ul>
        </nav>

<div style="display: flex;">
        Test
    <div style="flex: 0.1;height: 200px; background-color: #f4f5f8">

    </div>

    <div class="divider is-vertical">And</div>
    <div style="flex: 1;height: 200px; background-color: #f4f5f8"></div>
    Test2
</div>
    </div>
</template>

<script>
import Languages from '@/components/Languages.vue';
export default {
    name: 'Dashboard',
}
</script>