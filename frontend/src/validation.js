import _ from 'lodash'

export function validate(project) {
    let results = []
    _.each(project.apps, (app) => check_app(app, results))
    return results
}

function check_app(app, results) {
    _.each(app.models, (model) => check_model(app, model, results))
}

function check_model(app, model, results) {
    _.each(model.fields, (field) => check_field(app, model, field, results))
}

function check_field(app, model, field, results) {
    let msgs = []
    if (field.type == 'DecimalField') {
        if (!field.attrs.max_digits) {
            msgs.push('max_digits is required')
        }
        if (!field.attrs.decimal_places) {
            msgs.push('decimal_places is required')
        }
    } 
    else if (field.type == 'FileField' || field.type == 'ImageField') {
        if (!field.attrs.upload_to) {
            msgs.push('upload_to is required')
        }
    }

    // Final:
    if (msgs.length > 0) {
        let field_key = `${app.name}.${model.name}.${field.name}`
        results.push({type:'field', 'id': field_key, message:field.type + ': ' + msgs.join(', ')})
    }
        
}
