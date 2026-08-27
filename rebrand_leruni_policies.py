from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML_FILES = [
    "privacy-policy.html",
    "privacy-policy.ko.html",
    "privacy-policy.es.html",
    "privacy-policy.ja.html",
    "privacy-policy.zh.html",
    "account-deletion.html",
    "delete-account.html",
]

for name in HTML_FILES:
    path = ROOT / name
    source = path.read_text(encoding="utf-8")
    source = source.replace("Tokki", "LERUNI")
    source = source.replace("🐰 ", "")
    path.write_text(source, encoding="utf-8")
    print(f"[leruni-policies] branded {name}")

# English privacy: rewarded ads remain optional, but never buy extra chat turns.
p = ROOT / "privacy-policy.html"
s = p.read_text(encoding="utf-8")
s = s.replace(
    "Last updated: June 13, 2026",
    "Last updated: August 27, 2026",
)
s = s.replace(
    "Free users may choose to watch rewarded ads for extra chat turns. LERUNI uses Google Mobile Ads / AdMob only for this optional reward flow. We do not sell personal data, and paid tiers can avoid the free-turn ad flow. Ad requests may involve Google processing ad-related identifiers for delivery and measurement, subject to consent controls and platform settings where required.",
    "LERUNI may offer optional rewarded ads in non-chat features, such as an extra Keycap session. Rewarded ads do not extend the one-time chat preview and do not replace a subscription. We do not sell personal data. Ad requests may involve Google processing ad-related identifiers for delivery and measurement, subject to consent controls and platform settings where required.",
)
p.write_text(s, encoding="utf-8")

# Korean privacy.
p = ROOT / "privacy-policy.ko.html"
s = p.read_text(encoding="utf-8")
s = s.replace("최종 수정일: 2026년 6월 13일", "최종 수정일: 2026년 8월 27일")
s = s.replace(
    "무료 이용자는 추가 채팅 턴을 받기 위해 선택적으로 보상형 광고를 시청할 수 있습니다. 이 기능을 위해 Google Mobile Ads / AdMob SDK를 사용합니다. LERUNI는 개인정보를 판매하지 않으며, 유료 이용자는 무료 턴 광고 흐름을 이용하지 않아도 됩니다. 광고 요청 과정에서 Google이 광고 제공 및 측정에 필요한 광고 관련 식별자를 처리할 수 있으며, 필요한 경우 동의 설정과 플랫폼 설정이 적용됩니다.",
    "LERUNI는 키캡 추가 세션 등 채팅 외 기능에서 선택형 보상 광고를 제공할 수 있습니다. 보상 광고는 최초 1회 대화 체험을 연장하지 않으며 구독을 대신하지 않습니다. LERUNI는 개인정보를 판매하지 않습니다. 광고 요청 과정에서 Google이 광고 제공 및 측정에 필요한 광고 관련 식별자를 처리할 수 있으며, 필요한 경우 동의 설정과 플랫폼 설정이 적용됩니다.",
)
p.write_text(s, encoding="utf-8")

# Spanish privacy.
p = ROOT / "privacy-policy.es.html"
s = p.read_text(encoding="utf-8")
s = s.replace("Última actualización: 13 de junio de 2026", "Última actualización: 27 de agosto de 2026")
s = s.replace(
    "Los usuarios gratuitos pueden elegir ver anuncios recompensados para obtener turnos de chat adicionales. Para esta función, LERUNI usa Google Mobile Ads / AdMob SDK. LERUNI no vende datos personales, y los planes de pago pueden evitar este flujo de anuncios para turnos gratuitos. En las solicitudes de anuncios, Google puede procesar identificadores relacionados con publicidad para entrega y medición, sujeto a controles de consentimiento y ajustes de la plataforma cuando corresponda.",
    "LERUNI puede ofrecer anuncios recompensados opcionales en funciones que no son de chat, por ejemplo una sesión adicional de Keycap. Los anuncios recompensados no amplían la única vista previa de chat ni sustituyen una suscripción. LERUNI no vende datos personales. En las solicitudes de anuncios, Google puede procesar identificadores relacionados con publicidad para entrega y medición, sujeto a controles de consentimiento y ajustes de la plataforma cuando corresponda.",
)
p.write_text(s, encoding="utf-8")

# Japanese privacy.
p = ROOT / "privacy-policy.ja.html"
s = p.read_text(encoding="utf-8")
s = s.replace("最終更新日: 2026年6月13日", "最終更新日: 2026年8月27日")
s = s.replace(
    "無料ユーザーは、追加のチャット回数を得るために任意でリワード広告を視聴できます。この機能のためにGoogle Mobile Ads / AdMob SDKを使用します。LERUNIは個人データを販売せず、有料プランでは無料回数向けの広告フローを利用する必要はありません。広告リクエストでは、Googleが広告配信および測定に必要な広告関連識別子を処理する場合があり、必要に応じて同意設定とプラットフォーム設定が適用されます。",
    "LERUNIは、Keycapの追加セッションなどチャット以外の機能で任意のリワード広告を提供する場合があります。リワード広告で初回のチャットプレビューを延長することはできず、サブスクリプションの代わりにはなりません。LERUNIは個人データを販売しません。広告リクエストでは、Googleが広告配信および測定に必要な広告関連識別子を処理する場合があり、必要に応じて同意設定とプラットフォーム設定が適用されます。",
)
p.write_text(s, encoding="utf-8")

# Chinese privacy.
p = ROOT / "privacy-policy.zh.html"
s = p.read_text(encoding="utf-8")
s = s.replace("最后更新: 2026年6月13日", "最后更新: 2026年8月27日")
s = s.replace(
    "免费用户可以选择观看激励广告以获得额外聊天次数。为提供此功能,LERUNI使用Google Mobile Ads / AdMob SDK。LERUNI不出售个人数据,付费用户无需使用免费次数广告流程。广告请求过程中,Google可能会处理广告投放与衡量所需的广告相关标识符,并在需要时适用同意设置和平台设置。",
    "LERUNI可能会在非聊天功能中提供可选激励广告,例如额外一次Keycap会话。激励广告不会延长一次性的聊天预览,也不能替代订阅。LERUNI不出售个人数据。广告请求过程中,Google可能会处理广告投放与衡量所需的广告相关标识符,并在需要时适用同意设置和平台设置。",
)
p.write_text(s, encoding="utf-8")

# Deletion pages: update public-brand metadata while preserving legacy package/URL IDs.
p = ROOT / "delete-account.html"
s = p.read_text(encoding="utf-8").replace("Last updated: June 13, 2026", "Last updated: August 27, 2026")
s = s.replace(
    "LERUNI is published as <strong>LERUNI</strong> on Google Play\n    with package name <code>chat.tokki.app</code>.",
    "LERUNI uses the existing Google Play app identity\n    with package name <code>chat.tokki.app</code>.",
)
p.write_text(s, encoding="utf-8")

p = ROOT / "account-deletion.html"
s = p.read_text(encoding="utf-8")
s = s.replace("2026년 4월 28일", "2026년 8월 27일")
s = s.replace("April 28, 2026", "August 27, 2026")
p.write_text(s, encoding="utf-8")

# Repository README is public-facing too. Keep the repository name/URLs as legacy
# technical identifiers but make the displayed project brand current.
p = ROOT / "README.md"
s = p.read_text(encoding="utf-8").replace("Tokki", "LERUNI")
p.write_text(s, encoding="utf-8")

# Guards: no visible legacy proper-case brand or obsolete chat-turn ad promise.
for name in HTML_FILES + ["README.md"]:
    source = (ROOT / name).read_text(encoding="utf-8")
    if "Tokki" in source:
        raise RuntimeError(f"legacy visible brand remains in {name}")
for name in ["privacy-policy.html", "privacy-policy.ko.html", "privacy-policy.es.html", "privacy-policy.ja.html", "privacy-policy.zh.html"]:
    source = (ROOT / name).read_text(encoding="utf-8")
    if "extra chat turns" in source or "추가 채팅 턴" in source or "turnos de chat adicionales" in source or "追加のチャット回数" in source or "额外聊天次数" in source:
        raise RuntimeError(f"obsolete rewarded-chat copy remains in {name}")

print("[leruni-policies] policy branch ready")
