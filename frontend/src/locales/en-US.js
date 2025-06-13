export default {
  // Common
  common: {
    confirm: 'Confirm',
    cancel: 'Cancel',
    save: 'Save',
    delete: 'Delete',
    edit: 'Edit',
    add: 'Add',
    search: 'Search',
    loading: 'Loading...',
    success: 'Success',
    error: 'Error',
    warning: 'Warning',
    info: 'Info',
    close: 'Close',
    back: 'Back',
    next: 'Next',
    previous: 'Previous',
    submit: 'Submit',
    reset: 'Reset',
    refresh: 'Refresh',
    export: 'Export',
    import: 'Import',
    download: 'Download',
    upload: 'Upload',
    view: 'View',
    more: 'More'
  },

  // Navigation
  nav: {
    home: 'Home',
    dashboard: 'Dashboard',
    analysis: 'Data Analysis',
    reports: 'Reports',
    dataWarehouse: 'Data Warehouse',
    settings: 'Settings',
    profile: 'Profile',
    logout: 'Logout'
  },

  // Home
  home: {
    title: 'Data Analysis Platform',
    subtitle: 'Smart · Efficient · Professional',
    description: 'Enterprise-level data analysis solution based on advanced algorithms\nLet data drive every decision you make',
    getStarted: 'Get Started',
    learnMore: 'Learn More',
    features: {
      title: 'Core Features',
      subtitle: 'Powerful data processing capabilities to meet all your analysis needs',
      dashboard: {
        title: 'Data Dashboard',
        description: 'Real-time monitoring of key business metrics through intuitive charts and data visualization'
      },
      analysis: {
        title: 'Multi-dimensional Analysis',
        description: 'Explore data patterns from multiple angles and discover hidden business insights'
      },
      reports: {
        title: 'Report Generation',
        description: 'Automatically create professional reports with support for multiple export formats'
      },
      prediction: {
        title: 'Predictive Analysis',
        description: 'Use machine learning algorithms to predict business trends and identify opportunities'
      }
    },
    stats: {
      users: 'Enterprise Users',
      stability: 'System Stability',
      support: 'Technical Support'
    }
  },

  // Login
  login: {
    title: 'Login',
    subtitle: 'Welcome Back',
    username: 'Username',
    password: 'Password',
    rememberMe: 'Remember Me',
    forgotPassword: 'Forgot Password?',
    loginButton: 'Login',
    noAccount: "Don't have an account?",
    register: 'Sign Up',
    loginSuccess: 'Login successful',
    loginFailed: 'Login failed',
    invalidCredentials: 'Invalid username or password',
    placeholder: {
      username: 'Enter username',
      password: 'Enter password'
    }
  },

  // Settings
  settings: {
    title: 'System Settings',
    subtitle: 'Personalize your experience',
    appearance: {
      title: 'Appearance Settings',
      theme: {
        label: 'Theme Mode',
        description: 'Choose your preferred interface theme',
        dark: 'Dark',
        light: 'Light',
        auto: 'Auto'
      },
      language: {
        label: 'Interface Language',
        description: 'Select interface display language'
      },
      animations: {
        label: 'Animations',
        description: 'Enable or disable interface animations'
      }
    },
    data: {
      title: 'Data Settings',
      autoRefresh: {
        label: 'Auto Refresh',
        description: 'Automatic data refresh interval',
        options: {
          off: 'Off',
          '30s': '30 seconds',
          '1m': '1 minute',
          '5m': '5 minutes',
          '10m': '10 minutes'
        }
      },
      cache: {
        label: 'Data Cache',
        description: 'Enable data caching to improve performance'
      },
      realTime: {
        label: 'Real-time Data',
        description: 'Enable real-time data push'
      }
    },
    notifications: {
      title: 'Notification Settings',
      desktop: {
        label: 'Desktop Notifications',
        description: 'Allow desktop notifications'
      },
      email: {
        label: 'Email Notifications',
        description: 'Receive email notifications for important events'
      },
      sound: {
        label: 'Sound Alerts',
        description: 'Play notification sounds'
      }
    },
    security: {
      title: 'Security Settings',
      autoLogout: {
        label: 'Auto Logout',
        description: 'Auto logout time when inactive',
        options: {
          never: 'Never',
          '15m': '15 minutes',
          '30m': '30 minutes',
          '1h': '1 hour',
          '2h': '2 hours'
        }
      },
      twoFactor: {
        label: 'Two-Factor Authentication',
        description: 'Enable two-factor authentication'
      },
      loginHistory: {
        label: 'Login History',
        description: 'Record login history'
      }
    },
    actions: {
      save: 'Save Settings',
      saving: 'Saving...',
      reset: 'Reset to Default',
      clearCache: 'Clear Cache'
    },
    messages: {
      updated: 'Settings updated',
      saved: 'Settings saved successfully!',
      resetSuccess: 'Settings reset to default',
      cacheCleared: 'Cache cleared successfully!',
      updateFailed: 'Failed to update settings',
      saveFailed: 'Save failed, please try again',
      resetFailed: 'Failed to reset settings',
      cacheClearFailed: 'Failed to clear cache',
      loadFailed: 'Failed to load settings'
    }
  },

  // Search
  search: {
    placeholder: 'Search reports, analysis, users...',
    noResults: 'No results found',
    suggestions: 'Suggestions',
    recent: 'Recent searches',
    clear: 'Clear search'
  },

  // User menu
  user: {
    profile: 'Profile',
    settings: 'Settings',
    help: 'Help',
    logout: 'Logout',
    role: {
      admin: 'Administrator',
      user: 'User',
      guest: 'Guest'
    }
  },

  // Error messages
  errors: {
    networkError: 'Network connection error',
    serverError: 'Server error',
    notFound: 'Page not found',
    unauthorized: 'Unauthorized access',
    forbidden: 'Access forbidden',
    timeout: 'Request timeout',
    unknown: 'Unknown error'
  }
}
