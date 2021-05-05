<template>
  <nav class="pagination is-small" role="navigation" aria-label="pagination">
    <ul class="pagination-list">
      <li class="page-item">
        <a class="pagination-previous" href="javascript:void(0)" @click="prev">{{ $t("Previous") }}</a>
      </li>
      <li class="page-item">
        <a class="pagination-next" href="javascript:void(0)" @click="next">{{ $t("Next") }}</a>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import {ref} from 'vue';
export default {
  name: "Paginator",
  emits: ['page-changed'],
  props: {
    lastPage: Number,
  },
  setup(props, {emit}) {
    const page = ref(1);
    const next = async () => {
      if (page.value === props.lastPage) return;
      page.value++;
      emit('page-changed', page.value);
    }
    const prev = async () => {
      if (page.value === 1) return;
      page.value--;
      emit('page-changed', page.value);
    }
    return {
      next,
      prev
    }
  }
}
</script>