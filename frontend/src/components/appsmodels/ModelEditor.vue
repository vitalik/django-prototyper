<template>
    <div class="settings">
        <h2>{{ app.name }}.{{ model.name }}</h2>
        <hr>
        <fields-editor :model="model"></fields-editor>
    </div>
</template>

<script>
import { store } from '../../store'
import FieldsEditor from './FieldsEditor'


export default {
    name: 'modeleditor',
    computed: {
        app() {
            return store.app_get(this.$route.params.app)
        },
        model() {
            return store.models_get(this.app.name, this.$route.params.model)
        }
    },
    components: {
        FieldsEditor,
    }
}
</script>

