const js = require('@eslint/js');
const airbnbBase = require('eslint-config-airbnb-base');
const pluginJest = require('eslint-plugin-jest');

module.exports = [
  js.configs.recommended,
  ...airbnbBase(),
  ...pluginJest.configs.recommended,
  {
    files: ['*.js'],
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
    },
    settings: {
      jest: {
        version: 26,
      },
    },
    plugins: {
      jest: pluginJest,
    },
    rules: {
      'max-classes-per-file': 'off',
      'no-underscore-dangle': 'off',
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        {
          selector: 'LabeledStatement',
          message: 'Labels are a form of GOTO; using them makes code confusing and hard to maintain and understand.',
        },
        {
          selector: 'WithStatement',
          message: '`with` is disallowed in strict mode because it makes code impossible to predict and optimize.',
        },
      ],
    },
  },
];
