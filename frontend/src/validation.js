import _ from 'lodash'

export function validate(project) {
    let results = []
    _.each(project.apps, (app) => check_app(app, results))
    console.info(results)
    return results
}

function check_app(app, results) {
    _.each(app.models, (model) => check_model(app, model, results))
}

function check_model(app, model, results) {
    _.each(model.fields, (field) => check_field(app, model, field, results))
}

function check_field(app, model, field, results) {
    let field_key = `${app.name}.${model.name}.${field.name}`
    if (field.type == 'DecimalField') {
        if (!field.attrs.max_digits) {
            results.push({type:'field', 'id': field_key, message:'DecimalField - max_digits is required'})
        }
        if (!field.attrs.decimal_places) {
            results.push({type:'field', 'id': field_key, message:'DecimalField - decimal_places is required'})
        }
    } 
    else if (field.type == 'FileField' || field.type == 'ImageField') {
        if (!field.attrs.upload_to) {
            results.push({type:'field', 'id': field_key, message:field.type + ' upload_to is required'})
        }
    }
}
