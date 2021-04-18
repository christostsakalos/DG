<template>
    <div class="page-my-account">
        <h1 class="title">My account</h1>

        <Logout />
    </div>
</template>

<script>
  import Logout from '@/components/buttons/Logout'

export default {
    name: 'MyAccount',
    components: {
      Logout
    },
}
</script>