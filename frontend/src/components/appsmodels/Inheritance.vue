<template>
    <modal title="Inheritance" @close="$emit('close')"> <!-- @close="edit_colors=false" -->
        {{model.name}}
    </modal>
</template>

<script>

//import { store } from '../../store'
import Modal from '../utils/Modal'

export default {
    name: 'inheritance',
    props: {
        model: {
            required: true,
            type: Object
        }
    },
    computed: {

    },
    methods: {

    },
    components: {
        Modal,
    }
}
</script>

