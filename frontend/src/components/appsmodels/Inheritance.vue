<template>
    <modal title="Inheritance" @close="$emit('close')">
        <div class="row">
            <div class="col">

                <div class="mb-3">
                    Selected models:
                </div>

                <strong v-if="selected_models.length == 0">models.Model</strong>
                
                
                
                <draggable v-model="selected_models">
                    <button v-for="mdl in selected_models" @click="deselect(mdl)" class="btn btn-sm btn-block btn-outline-secondary text-left">
                        {{mdl}}
                    </button>
                </draggable>
            </div>
            <div class="col">
                <input v-model="search_keyword" class="form-control form-control-sm mb-2" placeholder="Search...">
                <button v-for="mdl in available_models" @click="select(mdl)" class="btn btn-sm btn-block btn-outline-secondary text-left">
                    &lt; &nbsp;
                    {{ mdl }}
                </button>
            </div>
        </div>
    </modal>
</template>

<script>

import _ from 'lodash'
import draggable from 'vuedraggable'
import { store } from '../../store'
import Modal from '../utils/Modal'


export default {
    name: 'inheritance',
    props: {
        model: {
            required: true,
            type: Object
        }
    },
    data() {
        return {
            search_keyword: '',
            selected_models: [],
        }
    },
    mounted() {
        if (this.model.inheritance === undefined) {
            this.selected_models = []
        } else {
            this.selected_models = this.model.inheritance
        }
    },
    computed: {
        available_models() {
            return _.filter(store.models_keys(), (k) => {
                if (_.indexOf(this.selected_models, k) != -1)
                    return false
                if (this.search_keyword.length == 0)
                    return true
                return _.includes(k.toLowerCase(), this.search_keyword.toLowerCase())
            })
        }
    },
    watch: {
        model() {
            if (this.model.inheritance === undefined) {
                this.selected_models = []
            } else {
                this.selected_models = this.model.inheritance
            }
        },
        selected_models() {
            this.$set(this.model, 'inheritance', this.selected_models)
        }
    },
    methods: {
        select(model) {
            this.selected_models.push(model)
        },
        deselect(key) {
            this.selected_models = _.filter(this.selected_models, k => k != key)
        }
    },
    components: {
        Modal,
        draggable,
    }
}
</script>

