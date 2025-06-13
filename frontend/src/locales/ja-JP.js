export default {
  // 共通
  common: {
    appName: 'データ分析プラットフォーム',
    confirm: '確認',
    cancel: 'キャンセル',
    save: '保存',
    delete: '削除',
    edit: '編集',
    add: '追加',
    search: '検索',
    loading: '読み込み中...',
    success: '成功',
    error: 'エラー',
    warning: '警告',
    info: '情報',
    close: '閉じる',
    back: '戻る',
    next: '次へ',
    previous: '前へ',
    submit: '送信',
    reset: 'リセット',
    refresh: '更新',
    export: 'エクスポート',
    import: 'インポート',
    download: 'ダウンロード',
    upload: 'アップロード',
    view: '表示',
    more: 'もっと見る'
  },

  // ナビゲーション
  nav: {
    home: 'ホーム',
    dashboard: 'ダッシュボード',
    analysis: '分析',
    reports: 'レポート',
    dataScreen: 'データ画面',
    dataWarehouse: 'データ倉庫',
    settings: '設定',
    profile: 'プロフィール',
    logout: 'ログアウト'
  },

  // ホーム
  home: {
    title: 'データ分析プラットフォーム',
    subtitle: 'スマート・効率的・プロフェッショナル',
    description: '先進的なアルゴリズムに基づく企業レベルのデータ分析ソリューション\nデータがあなたのすべての決定を導きます',
    getStarted: '今すぐ始める',
    learnMore: '詳細を見る',
    features: {
      title: 'コア機能',
      subtitle: '強力なデータ処理能力で、あらゆる分析ニーズに対応',
      dashboard: {
        title: 'データダッシュボード',
        description: '直感的なチャートとデータ可視化により、重要なビジネス指標をリアルタイムで監視'
      },
      analysis: {
        title: '多次元分析',
        description: '複数の角度からデータパターンを探索し、隠れたビジネス洞察を発見'
      },
      reports: {
        title: 'レポート生成',
        description: '複数の出力形式をサポートし、プロフェッショナルなレポートを自動作成'
      },
      prediction: {
        title: '予測分析',
        description: '機械学習アルゴリズムを使用してビジネストレンドを予測し、機会を特定'
      }
    },
    stats: {
      users: '企業ユーザー',
      stability: 'システム安定性',
      support: 'テクニカルサポート'
    }
  },

  // ログイン
  login: {
    title: 'ログイン',
    subtitle: 'おかえりなさい',
    username: 'ユーザー名',
    password: 'パスワード',
    rememberMe: 'ログイン状態を保持',
    forgotPassword: 'パスワードを忘れましたか？',
    loginButton: 'ログイン',
    noAccount: 'アカウントをお持ちでないですか？',
    register: '今すぐ登録',
    loginSuccess: 'ログイン成功',
    loginFailed: 'ログイン失敗',
    invalidCredentials: 'ユーザー名またはパスワードが間違っています',
    placeholder: {
      username: 'ユーザー名を入力',
      password: 'パスワードを入力'
    }
  },

  // 設定
  settings: {
    title: 'システム設定',
    subtitle: 'あなたの体験をパーソナライズ',
    appearance: {
      title: '外観設定',
      theme: {
        label: 'テーマモード',
        description: 'お好みのインターフェーステーマを選択',
        dark: 'ダーク',
        light: 'ライト',
        auto: '自動'
      },
      language: {
        label: 'インターフェース言語',
        description: 'インターフェース表示言語を選択'
      },
      animations: {
        label: 'アニメーション',
        description: 'インターフェースアニメーションを有効または無効にする'
      }
    },
    data: {
      title: 'データ設定',
      autoRefresh: {
        label: '自動更新',
        description: 'データの自動更新間隔',
        options: {
          off: 'オフ',
          '30s': '30秒',
          '1m': '1分',
          '5m': '5分',
          '10m': '10分'
        }
      },
      cache: {
        label: 'データキャッシュ',
        description: 'パフォーマンス向上のためデータキャッシュを有効にする'
      },
      realTime: {
        label: 'リアルタイムデータ',
        description: 'リアルタイムデータプッシュを有効にする'
      }
    },
    notifications: {
      title: '通知設定',
      desktop: {
        label: 'デスクトップ通知',
        description: 'デスクトップ通知を許可'
      },
      email: {
        label: 'メール通知',
        description: '重要なイベントのメール通知を受信'
      },
      sound: {
        label: 'サウンドアラート',
        description: '通知音を再生'
      }
    },
    security: {
      title: 'セキュリティ設定',
      autoLogout: {
        label: '自動ログアウト',
        description: '非アクティブ時の自動ログアウト時間',
        options: {
          never: 'なし',
          '15m': '15分',
          '30m': '30分',
          '1h': '1時間',
          '2h': '2時間'
        }
      },
      twoFactor: {
        label: '二要素認証',
        description: '二要素認証を有効にする'
      },
      loginHistory: {
        label: 'ログイン履歴',
        description: 'ログイン履歴を記録'
      }
    },
    actions: {
      save: '設定を保存',
      saving: '保存中...',
      reset: 'デフォルトにリセット',
      clearCache: 'キャッシュをクリア'
    },
    messages: {
      updated: '設定が更新されました',
      saved: '設定が正常に保存されました！',
      resetSuccess: '設定がデフォルトにリセットされました',
      cacheCleared: 'キャッシュが正常にクリアされました！',
      updateFailed: '設定の更新に失敗しました',
      saveFailed: '保存に失敗しました。もう一度お試しください',
      resetFailed: '設定のリセットに失敗しました',
      cacheClearFailed: 'キャッシュのクリアに失敗しました',
      loadFailed: '設定の読み込みに失敗しました'
    }
  },

  // 検索
  search: {
    placeholder: 'レポート、分析、ユーザーを検索...',
    noResults: '結果が見つかりません',
    suggestions: '提案',
    recent: '最近の検索',
    clear: '検索をクリア'
  },

  // ユーザーメニュー
  user: {
    defaultName: 'ユーザー',
    profile: 'プロフィール',
    settings: '設定',
    help: 'ヘルプ',
    logout: 'ログアウト',
    role: {
      admin: '管理者',
      user: 'ユーザー',
      guest: 'ゲスト'
    }
  },

  // エラーメッセージ
  errors: {
    networkError: 'ネットワーク接続エラー',
    serverError: 'サーバーエラー',
    notFound: 'ページが見つかりません',
    unauthorized: '未認証のアクセス',
    forbidden: 'アクセスが禁止されています',
    timeout: 'リクエストタイムアウト',
    unknown: '不明なエラー'
  }
}
