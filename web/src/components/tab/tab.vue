<template>
  <div class="tab">
    <div v-for="item in titles" :key="item" class="tab-item" :class="{ 'selected': currentSelected === item }"
      @click="clickTabItem(item)">
      {{ item }}
    </div>
  </div>
</template>

<script>
export default {
  props: {
    titles: Array,
    firstSelected: String
  },
  data () {
    return {
      selected: ''
    }
  },
  computed: {
    currentSelected () {
      if (this.selected.length > 0) {
        return this.selected
      } else {
        return this.firstSelected
      }
    }
  },
  methods: {
    clickTabItem (item) {
      this.selected = item
      this.$emit('input', item)
    }
  }
}
</script>

<style>
.tab {
  display: flex;
  height: 40px;
  line-height: 40px;
}
.tab-item {
  flex: 1;
  text-align: center;
}
.tab-item.selected {
  color: dodgerblue;
  border-bottom: 1px solid skyblue;
}
</style>
